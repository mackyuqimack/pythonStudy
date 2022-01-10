# -*- coding: utf8 -*-
import json
import time
import traceback

import requests

token = "01e1e4eb2db8462e9a5a6a273aacf255"
push_plus_url = "https://www.pushplus.plus/send"
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
    try:
        requests.post(url=push_plus_url, headers=form_header, data=msg_data)
    except requests.exceptions.RequestException as exception:
        print(exception)


def get_lovelive_info():
    """
    从土味情话中获取每日一句。
    :return: str,土味情话。
    """
    print('获取土味情话...')
    try:
        resp = requests.get('https://api.lovelive.tools/api/SweetNothings')
        if resp.status_code == 200:
            return resp.text
        print('土味情话获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
    return None

def get_holiday():
    """
    获取节假日信息
    :return: flag:1=工作，0=休息,name:当前日期。
    """
    print("获取节假日信息...")
    holiday_url = "https://timor.tech/api/holiday/info/"
    now = time.strftime("%Y-%m-%d", time.localtime())
    target_url = holiday_url + now
    try:
        resp = requests.get(target_url)
        if resp.status_code == 200:
            resp_json = resp.json()
            if resp_json["code"] == 0:
                resp_type = resp_json['type']
                # 节假日类型，分别表示工作日、周末、节日、调休。
                type = resp_type['type']
                # 1上班 0休息
                flag = 0
                if type == 0 or type == 3:
                    flag = 1
                name = resp_type['name']
                return flag, name
        print('节假日信息获取失败。')
    except:
        print('节假日信息获取异常。')
        traceback.print_exc()
    return 1, ""

def main():
    flag, name = get_holiday()
    if flag == 1:
        title = get_lovelive_info()
        send_msg(title, name + "指尖上的学霸晚上答题")


def main_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("Received context: " + str(context))
    print("Hello world")
    main()
    return ("Hello World")
