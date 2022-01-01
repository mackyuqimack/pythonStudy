import traceback

import requests
from lovelive import get_one_words

token = "60df29e93eae4420a4f96cec21b4d66b"
push_plus_url = "http://www.pushplus.plus/send"
form_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}


def send_msg(title, msg):
    """
    发送push plus推送消息
    :param title 标题
    :param msg: 消息内容
    """
    msg_data = {
        "token": token,
        "title": title,
        "content": msg,
        "template": "txt"
    }
    if push_plus_url is None or len(push_plus_url.strip()) == 0:
        print("未填入发送信息地址，将不发送消息提醒。")
        print(msg)
        input('Press any key to quit program.')
    else:
        requests.post(url=push_plus_url, headers=form_header, data=msg_data)


def main():
    title = get_one_words()
    send_msg(title, "指尖上的学霸晚上答题")


if __name__ == '__main__':
    try:
        main()
    except:
        traceback.print_exc()
        input('Press any key to quit program.')
