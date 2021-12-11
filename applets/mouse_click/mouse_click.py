from util.log import logger
import win32con
import win32api
import time

seconds = 60 * 10
i = 1
logger.info(f"每{seconds}秒执行一次鼠标左键单击操作")
while True:
    logger.info(f"第{i}次执行")
    win32api.SetCursorPos((0, 0))
    # 左键单击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(seconds)
    i += 1
