"""微信群发消息"""

import os
import time
import subprocess
import uiautomation as auto
from typing import Iterable

"""
    示例：
    wx = WxOperation()
    # 发送文本
    wx.send_msg(
        '文件传输助手',
        msgs=['hello', 'world']
    )
    # 发送文件
    wx.send_msg(
        '文件传输助手',
        file_paths=['demo.bat', 'demo.png']
    )
    # 发送文本 + 文件
    wx.send_msg(
        '文件传输助手',
        msgs=['hello', 'world'],
        file_paths=['demo.bat', 'demo.png']
    )
    # 批量发送文本+文件
    wx.send_msg(
        *['文件传输助手', '靓仔'],	# 
        msgs=['hello', 'world'],
        file_paths=['demo.bat', 'demo.png']
    )
"""


class WxOperation:
    """微信群发消息的类。"""

    def __init__(self):
        auto.SendKeys(text='{Alt}{Ctrl}w')  # 快捷键唤醒微信
        self.wx_window = auto.WindowControl(Name='微信', ClassName='WeChatMainWndForPC')
        assert self.wx_window.Exists(), "窗口不存在"
        self.input_edit = self.wx_window.EditControl(Name='输入')
        self.search_edit = self.wx_window.EditControl(Name='搜索')

    def __goto_chat_box(self, name: str) -> None:
        """跳转到指定 name好友的聊天窗口"""
        assert name, "无法跳转到名字为空的聊天窗口"
        self.wx_window.SendKeys(text='{Ctrl}f', waitTime=0.2)
        self.wx_window.SendKeys(text='{Ctrl}a', waitTime=0.1)
        self.wx_window.SendKey(key=auto.SpecialKeyNames['DELETE'])
        self.search_edit.SendKeys(text=name, waitTime=0.5)
        self.wx_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=0.2)

    def __send_text(self, *msgs) -> None:
        """发送文本"""
        for msg in msgs:
            assert msg, "发送的文本内容为空"
            self.input_edit.SendKeys(text='{Ctrl}a', waitTime=0.1)
            self.input_edit.SendKey(key=auto.SpecialKeyNames['DELETE'])
            # self.input_edit.SendKeys(text=msg, waitTime=0.1) # 一个个字符插入,不建议使用该方法
            # 设置到剪切板再黏贴到输入框
            auto.SetClipboardText(text=msg)
            self.input_edit.SendKeys(text='{Ctrl}v', waitTime=0.1)
            self.wx_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=0.2)

    def __send_file(self, *file_paths) -> None:
        """发送文件"""
        all_path = str()
        for path in file_paths:
            full_path = os.path.abspath(path=path)
            assert os.path.exists(full_path), f"{full_path} 文件路径有误"
            all_path += "'" + full_path + "',"
        args = ['powershell', f'Get-Item {all_path[:-1]} | Set-Clipboard']
        subprocess.Popen(args=args)
        time.sleep(0.5)
        self.input_edit.SendKeys(text='{Ctrl}v', waitTime=0.2)
        self.wx_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=0.2)

    def send_msg(self, *names: str or Iterable, msgs: Iterable = None, file_paths: Iterable = None) -> None:
        """发送消息，可同时发送文本和文件（至少选一项"""
        assert names, "用户名列表为空"
        assert any([msgs, file_paths]), "没有发送任何消息"
        assert not isinstance(msgs, str), "文本必须为可迭代且非字符串类型"
        assert not isinstance(file_paths, str), "文件路径必须为可迭代且非字符串类型"
        for name in names:
            self.__goto_chat_box(name=name)
            if msgs:
                self.__send_text(*msgs)
            if file_paths:
                self.__send_file(*file_paths)


if __name__ == '__main__':
    wx = WxOperation()
    # 发送文本
    wx.send_msg(
        '文件传输助手',
        msgs=['hello']
    )