import time

import uiautomation as auto


def send_msg(content, chat_user):
    # 唤醒家园
    auto.SendKeys(text='{Ctrl}{Shift}s')
    yg_window = auto.PaneControl(Name='YGHome', ClassName='Chrome_WidgetWin_1')
    if not yg_window.Exists():
        auto.SendKeys(text='{Ctrl}{Shift}s')
    assert yg_window.Exists(), "窗口不存在"

    message = yg_window.GroupControl(Name='消息')
    message.DoubleClick()
    time.sleep(1)

    search = yg_window.EditControl(Name='按姓名/群名搜索')
    search.DoubleClick()
    search.SendKeys(chat_user)
    time.sleep(1)

    search.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=0.2)
    edit = message.GetParentControl().GroupControl(Name='', AutomationId='msg-chat-input-editor-content')
    # edit.SetFocus()
    # time.sleep(2)
    # yg_window.SendKeys(text='{Ctrl}a')
    # yg_window.SendKey(key=auto.SpecialKeyNames['DELETE'])

    edit.SendKeys(content)
    time.sleep(1)
    send = edit.GetParentControl().GetParentControl().ButtonControl(Name='发 送')
    send.DoubleClick()


if __name__ == '__main__':
    send_msg("内容", "李通")
