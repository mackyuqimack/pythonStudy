// ==UserScript==
// @name         V2EX 移动端用户标签
// @name:zh-CN   V2EX 移动端用户标签
// @version      1.0.0
// @description  在手机上给 V2EX 用户打标签并展示，与 PC 端 V2Next 脚本共用同一份记事本数据（--用户标签--），跨平台互通。
// @author       cdp-inject
// @match        https://v2ex.com/*
// @match        https://www.v2ex.com/*
// @match        https://*.v2ex.com/*
// @grant        GM_addStyle
// @run-at       document-idle
// ==/UserScript==

(function () {
    'use strict';

    // 与 PC 端 V2Next 脚本保持完全一致，才能读取/写入同一份记事本数据
    var TAG_PREFIX = '--用户标签--';

    // ---------- 全局状态 ----------
    var state = {
        // 当前登录用户名
        me: '',
        // 记事本子条目 id（存放标签的那条）
        noteId: '',
        // 标签数据：{ username: [tag1, tag2, ...] }
        tags: {},
        // 是否已从记事本加载
        loaded: false,
        loading: false
    };

    // ---------- 小工具 ----------
    function getOrigin() {
        return location.origin || (location.protocol + '//' + location.host);
    }

    function isLogin() {
        return !!state.me;
    }

    // 检测页面类型
    function detectPage() {
        var path = location.pathname;
        if (/^\/t\/\d+/.test(path)) return 'topic';        // 主题详情
        if (/^\/member\//.test(path)) return 'member';     // 用户主页
        if (/^\/go\//.test(path)) return 'node';           // 节点列表
        if (path === '/' || /^\/(recent|changes)/.test(path)) return 'home'; // 首页/最近
        return 'other';
    }

    // ---------- 网络请求（同源 fetch，自动携带 cookie，无需 GM 权限） ----------
    function httpGet(url) {
        return fetch(url, { credentials: 'same-origin' }).then(function (r) { return r.text(); });
    }

    function httpPost(url, formData) {
        return fetch(url, {
            method: 'POST',
            credentials: 'same-origin',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: formData
        }).then(function (r) {
            return { status: r.status, finalUrl: r.url || url };
        });
    }

    // ---------- 记事本（标签存储） ----------
    // 读取记事本列表，找到 --用户标签-- 对应的 id
    function findTagNoteId() {
        return httpGet(getOrigin() + '/notes').then(function (html) {
            var doc = new DOMParser().parseFromString(html, 'text/html');
            var links = doc.querySelectorAll('#Main .note_item_title a');
            for (var i = 0; i < links.length; i++) {
                var text = (links[i].textContent || '').trim();
                if (text.indexOf(TAG_PREFIX) === 0) {
                    var href = links[i].getAttribute('href') || '';
                    var m = href.match(/(\d+)\/?$/);
                    if (m) return m[1];
                }
            }
            return '';
        });
    }

    // 读取记事本内容并解析标签 JSON
    function readTagNote() {
        if (!state.noteId) return Promise.resolve({});
        return httpGet(getOrigin() + '/notes/edit/' + state.noteId).then(function (html) {
            var doc = new DOMParser().parseFromString(html, 'text/html');
            var ta = doc.querySelector('textarea[name="content"]');
            var text = ta ? ta.value : (doc.querySelector('.note_editor') || {}).textContent || '';
            if (text.indexOf(TAG_PREFIX) !== 0) return {};
            var jsonStr = text.substring(TAG_PREFIX.length).trim();
            if (!jsonStr) return {};
            try {
                var obj = JSON.parse(jsonStr);
                return (obj && typeof obj === 'object') ? obj : {};
            } catch (e) {
                return {};
            }
        });
    }

    // 创建记事本子条目，返回新 id
    function createTagNote() {
        var body = 'content=' + encodeURIComponent(TAG_PREFIX) + '&parent_id=0&syntax=0';
        return httpPost(getOrigin() + '/notes/new', body).then(function (r) {
            var m = (r.finalUrl || '').match(/(\d+)\/?$/);
            return m ? m[1] : '';
        });
    }

    // 把标签写回记事本（与 PC 端一致：前缀 + JSON.stringify）
    function saveTagsToNote(tags) {
        if (!state.noteId) return Promise.resolve(false);
        // 清理空数组的用户，保持数据干净
        Object.keys(tags).forEach(function (k) {
            if (!tags[k] || tags[k].length === 0) delete tags[k];
        });
        var content = TAG_PREFIX + JSON.stringify(tags);
        var body = 'content=' + encodeURIComponent(content) + '&syntax=0';
        return httpPost(getOrigin() + '/notes/edit/' + state.noteId, body).then(function (r) {
            // 编辑成功后通常会 302 回记事本页
            return true;
        });
    }

    // 识别登录用户（兼容桌面端 .tools 与移动端 #menu-entry）
    function detectLoginUser() {
        // 桌面端：顶部 .tools 里的 /member/ 链接
        var tools = document.querySelector('.tools');
        if (tools) {
            var links = tools.querySelectorAll('a[href^="/member/"]');
            for (var i = 0; i < links.length; i++) {
                var m = (links[i].getAttribute('href') || '').match(/^\/member\/([^\/]+)/);
                if (m) return m[1];
            }
        }
        // 移动端：菜单入口头像的 alt 属性
        var avatar = document.querySelector('#menu-entry img.avatar');
        if (avatar) {
            var alt = avatar.getAttribute('alt');
            if (alt) return alt;
        }
        // 移动端兜底：菜单里第一个 /member/ 链接
        var menuLink = document.querySelector('#site-header-menu a[href^="/member/"]');
        if (menuLink) {
            var m2 = (menuLink.getAttribute('href') || '').match(/^\/member\/([^\/]+)/);
            if (m2) return m2[1];
        }
        return '';
    }

    // 初始化：读取用户身份 + 加载标签
    function initData() {
        state.me = detectLoginUser();

        if (!isLogin()) return Promise.resolve();

        return findTagNoteId().then(function (id) {
            var p;
            if (id) {
                state.noteId = id;
                p = Promise.resolve();
            } else {
                // 不存在则创建（仅登录后）
                p = createTagNote().then(function (newId) {
                    if (newId) state.noteId = newId;
                });
            }
            return p.then(function () {
                return readTagNote().then(function (tags) {
                    state.tags = tags;
                    state.loaded = true;
                });
            });
        }).catch(function (e) {
            console.warn('[V2EX标签] 初始化失败', e);
        });
    }

    // ---------- UI：标签渲染 ----------
    // 给某个用户名链接后面渲染标签（只处理第一次）
    function renderTagsForLink(a, username, opts) {
        if (!a || !username) return;
        if (a.hasAttribute('data-v2m-tag')) return;
        a.setAttribute('data-v2m-tag', '1');

        var myTags = state.tags[username] || [];
        var wrap = document.createElement('span');
        wrap.className = 'v2m-tagwrap';

        // 标签 chip
        myTags.forEach(function (t) {
            var chip = document.createElement('span');
            chip.className = 'v2m-tag';
            chip.setAttribute('data-tag', t);
            var label = document.createElement('span');
            label.textContent = t;
            var del = document.createElement('i');
            del.className = 'v2m-del';
            del.textContent = '×';
            del.title = '删除标签';
            chip.appendChild(label);
            chip.appendChild(del);
            chip.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                removeTag(username, t);
            });
            wrap.appendChild(chip);
        });

        // 添加按钮（触屏友好，常显）
        if (opts && opts.showAdd !== false && isLogin()) {
            var add = document.createElement('button');
            add.type = 'button';
            add.className = 'v2m-add';
            add.textContent = '+';
            add.title = '添加标签';
            add.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                openAddModal(username);
            });
            wrap.appendChild(add);
        }

        // 插到用户名链接之后
        a.parentNode.insertBefore(wrap, a.nextSibling);
    }

    // 渲染主题详情页：主贴作者 + 每条回复作者（桌面端与移动端选择器一致）
    function renderTopicPage() {
        if (!state.loaded) return;

        // 主贴作者：small.gray 里的 /member/ 链接（两套模板结构相同）
        var authorA = document.querySelector('small.gray > a[href^="/member/"]');
        if (authorA) {
            renderTagsForLink(authorA, authorA.textContent.trim(), { showAdd: true });
        }

        // 回复作者：strong 里的 /member/ 链接（两套模板结构相同）
        var authors = document.querySelectorAll('strong > a[href^="/member/"]');
        authors.forEach(function (a) {
            renderTagsForLink(a, a.textContent.trim(), { showAdd: true });
        });
    }

    // 渲染列表页（首页/节点）：主题列表里 strong 的作者链接
    function renderListPage() {
        if (!state.loaded) return;
        var links = document.querySelectorAll('strong > a[href^="/member/"]');
        links.forEach(function (a) {
            renderTagsForLink(a, a.textContent.trim(), { showAdd: false });
        });
    }

    // 渲染用户主页
    function renderMemberPage() {
        if (!state.loaded) return;
        var h1 = document.querySelector('h1');
        if (h1) {
            var name = h1.textContent.trim();
            // 用户名在 V2EX 大小写不敏感，href 可能是小写，遍历匹配
            var links = document.querySelectorAll('a[href^="/member/"]');
            var target = null;
            for (var i = 0; i < links.length; i++) {
                var href = links[i].getAttribute('href') || '';
                var m = href.match(/^\/member\/([^\/]+)\/?$/);
                if (m && m[1].toLowerCase() === name.toLowerCase()) {
                    target = links[i];
                    break;
                }
            }
            if (target) renderTagsForLink(target, name, { showAdd: true });
        }
    }

    function render() {
        var page = detectPage();
        if (page === 'topic') renderTopicPage();
        else if (page === 'member') renderMemberPage();
        else if (page === 'home' || page === 'node') renderListPage();
    }

    // ---------- UI：添加/删除标签 ----------
    function removeTag(username, tag) {
        if (!confirm('删除对 ' + username + ' 的标签「' + tag + '」？')) return;
        var list = state.tags[username] || [];
        var idx = list.indexOf(tag);
        if (idx > -1) list.splice(idx, 1);
        state.tags[username] = list;
        persistAndRerender();
    }

    function addTag(username, tag) {
        tag = (tag || '').trim();
        if (!tag) { toast('请输入标签', 'warn'); return; }
        var list = state.tags[username] || [];
        if (list.indexOf(tag) > -1) { toast('标签已存在', 'warn'); return; }
        list.push(tag);
        state.tags[username] = list;
        persistAndRerender();
        return true;
    }

    function persistAndRerender() {
        saveTagsToNote(state.tags).then(function (ok) {
            if (!ok) toast('标签保存失败', 'error');
            rerenderAll();
        }).catch(function () {
            toast('标签保存失败', 'error');
        });
    }

    function rerenderAll() {
        // 清掉已渲染标记，重新渲染
        document.querySelectorAll('.v2m-tagwrap').forEach(function (n) { n.remove(); });
        document.querySelectorAll('[data-v2m-tag]').forEach(function (n) { n.removeAttribute('data-v2m-tag'); });
        render();
    }

    // ---------- UI：添加标签弹窗 ----------
    var modalEl = null;
    var modalUsername = '';

    function ensureModal() {
        if (modalEl) return;
        modalEl = document.createElement('div');
        modalEl.className = 'v2m-modal';
        modalEl.innerHTML =
            '<div class="v2m-mask"></div>' +
            '<div class="v2m-dialog">' +
            '  <div class="v2m-title">添加标签</div>' +
            '  <div class="v2m-user">用户：<b class="v2m-username"></b></div>' +
            '  <input class="v2m-input" type="text" placeholder="输入标签，回车确认" />' +
            '  <div class="v2m-btns">' +
            '    <button class="v2m-btn v2m-cancel" type="button">取消</button>' +
            '    <button class="v2m-btn v2m-ok" type="button">确定</button>' +
            '  </div>' +
            '</div>';
        document.body.appendChild(modalEl);

        var input = modalEl.querySelector('.v2m-input');
        modalEl.querySelector('.v2m-mask').addEventListener('click', closeModal);
        modalEl.querySelector('.v2m-cancel').addEventListener('click', closeModal);
        modalEl.querySelector('.v2m-ok').addEventListener('click', function () {
            if (addTag(modalUsername, input.value)) closeModal();
        });
        input.addEventListener('keydown', function (e) {
            if (e.key === 'Enter') {
                if (addTag(modalUsername, input.value)) closeModal();
            }
        });
    }

    function openAddModal(username) {
        ensureModal();
        modalUsername = username;
        modalEl.querySelector('.v2m-username').textContent = username;
        modalEl.querySelector('.v2m-input').value = '';
        modalEl.classList.add('show');
        setTimeout(function () { modalEl.querySelector('.v2m-input').focus(); }, 50);
    }

    function closeModal() {
        if (modalEl) modalEl.classList.remove('show');
    }

    // ---------- UI：轻提示 ----------
    var toastEl = null;
    function toast(text, type) {
        if (!toastEl) {
            toastEl = document.createElement('div');
            toastEl.className = 'v2m-toast';
            document.body.appendChild(toastEl);
        }
        toastEl.textContent = text;
        toastEl.className = 'v2m-toast ' + (type || 'ok');
        toastEl.classList.add('show');
        clearTimeout(toast._t);
        toast._t = setTimeout(function () { toastEl.classList.remove('show'); }, 1800);
    }

    // ---------- 移动端视口优化 ----------
    // V2EX 默认没有 viewport meta，手机访问会被当成桌面宽度缩放。
    // 仅在移动端补一个 viewport，让页面按设备宽度渲染并允许双指缩放。
    function isMobileDevice() {
        return /Android|iPhone|iPad|iPod|Mobile|BlackBerry|IEMobile/i.test(navigator.userAgent) ||
            (navigator.maxTouchPoints > 1 && window.innerWidth < 768) ||
            window.innerWidth < 560;
    }

    function ensureViewport() {
        if (!isMobileDevice()) return;
        var meta = document.querySelector('meta[name="viewport"]');
        if (!meta) {
            meta = document.createElement('meta');
            meta.name = 'viewport';
            meta.content = 'width=device-width, initial-scale=1';
            document.head.appendChild(meta);
        }
    }

    // ---------- 动态内容监听 ----------
    var scanTimer = null;
    function scheduleRender() {
        if (scanTimer) return;
        scanTimer = setTimeout(function () {
            scanTimer = null;
            render();
        }, 200);
    }

    function watchDom() {
        var mo = new MutationObserver(function () {
            scheduleRender();
        });
        mo.observe(document.body, { childList: true, subtree: true });
    }

    // ---------- 样式 ----------
    function addStyles() {
        var css = [
            '.v2m-tagwrap{display:inline-flex;align-items:center;flex-wrap:wrap;gap:4px;margin:0 0 0 6px;vertical-align:middle;font-weight:normal;font-style:normal;}',
            '.v2m-tag{display:inline-flex;align-items:center;gap:3px;background:#f0f4ff;color:#2f6fed;border:1px solid #c9d9ff;border-radius:10px;padding:1px 7px;font-size:12px;line-height:16px;cursor:default;max-width:140px;}',
            '.v2m-tag span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}',
            '.v2m-del{font-style:normal;color:#94a3b8;font-size:13px;cursor:pointer;padding:0 2px;border-radius:50%;line-height:14px;}',
            '.v2m-del:hover{color:#ef4444;background:#fee2e2;}',
            '.v2m-add{box-sizing:border-box;min-width:20px;height:20px;padding:0 4px;border:1px dashed #94a3b8;border-radius:10px;background:transparent;color:#64748b;font-size:14px;line-height:18px;cursor:pointer;}',
            '.v2m-add:active{background:#eef2ff;}',
            '.v2m-modal{display:none;position:fixed;inset:0;z-index:2147483000;}',
            '.v2m-modal.show{display:block;}',
            '.v2m-mask{position:absolute;inset:0;background:rgba(15,23,42,.45);}',
            '.v2m-dialog{position:absolute;left:50%;top:45%;transform:translate(-50%,-50%);width:86%;max-width:340px;background:#fff;border-radius:14px;padding:18px 16px;box-shadow:0 10px 40px rgba(0,0,0,.25);box-sizing:border-box;}',
            '.v2m-title{font-size:16px;font-weight:700;color:#0f172a;margin-bottom:10px;}',
            '.v2m-user{font-size:13px;color:#64748b;margin-bottom:10px;word-break:break-all;}',
            '.v2m-user b{color:#334155;}',
            '.v2m-input{box-sizing:border-box;width:100%;height:40px;border:1px solid #e2e8f0;border-radius:8px;padding:0 12px;font-size:14px;outline:none;background:#f8fafc;}',
            '.v2m-input:focus{border-color:#2f6fed;background:#fff;}',
            '.v2m-btns{display:flex;justify-content:flex-end;gap:10px;margin-top:16px;}',
            '.v2m-btn{height:36px;padding:0 18px;border-radius:8px;border:1px solid #e2e8f0;background:#fff;color:#334155;font-size:14px;cursor:pointer;}',
            '.v2m-btn.v2m-ok{background:#2f6fed;border-color:#2f6fed;color:#fff;}',
            '.v2m-toast{position:fixed;left:50%;bottom:18%;transform:translateX(-50%) translateY(20px);background:rgba(15,23,42,.9);color:#fff;font-size:14px;padding:10px 18px;border-radius:20px;z-index:2147483001;opacity:0;transition:all .2s;pointer-events:none;max-width:80%;}',
            '.v2m-toast.show{opacity:1;transform:translateX(-50%) translateY(0);}',
            '.v2m-toast.warn{background:rgba(202,138,4,.95);}',
            '.v2m-toast.error{background:rgba(220,38,38,.95);}'
        ].join('\n');

        if (typeof GM_addStyle === 'function') {
            GM_addStyle(css);
        } else {
            var style = document.createElement('style');
            style.textContent = css;
            document.head.appendChild(style);
        }
    }

    // ---------- 启动 ----------
    function boot() {
        addStyles();
        ensureViewport();
        watchDom();

        // 登录状态由 initData 内部判断（未登录则跳过加载与渲染）
        initData().then(function () {
            render();
        });
    }

    // 等待 DOM 就绪
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', boot);
    } else {
        boot();
    }
})();
