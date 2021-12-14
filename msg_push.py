#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/12  11:13 上午
@Author  : Frank.lian
@File    : msg_push.py
@Description :
'''
import json
import os

import requests


def dd_msg_push(webhook):
    """
    钉钉消息推送
    :param webhook: 钉钉机器人webhookurl
    """
    d = {}
    proDir = os.path.abspath(os.path.dirname((__file__)))
    f = open(proDir + '/report/html/export/prometheusData.txt', 'r')
    for lines in f:
        for c in lines:
            launch_name = lines.strip('\n').split(' ')[0]
            num = lines.strip('\n').split(' ')[1]
            d.update({launch_name: num})
    retries_run = d.get('launch_retries_run')  # 运行总数
    status_passed = d.get('launch_status_passed')  # 通过数量
    status_failed = d.get('launch_status_failed')  # 不通过数量
    '''
    钉钉推送
    '''
    con = {"msgtype": "text",
           "text": {
               "content": "智语2.0线上接口自动化脚本完成。\n测试概述:\n运行总数:" + retries_run + "\n通过数量:" + status_passed + "\n失败数量:" + status_failed + "\n构建地址：\n" + "job_url" + "\n报告地址：\n" + "report_url"}
           }
    requests.post(webhook, data=json.dumps(con), headers={'Content-Type': 'application/json'})
