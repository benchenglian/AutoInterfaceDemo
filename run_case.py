#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/12  11:02 上午
@Author  : Frank.lian
@File    : run_case.py
@Description :case执行。
'''
import subprocess

from common.logger import Logger
logger = Logger(logger="Run_Test").getlog()

def init_run_UI_Test():
    cmd = "python3 -m pytest -sq testcases/ --alluredir report/xml"
    subprocess.call(cmd, shell=True)
    logger.info("执行接口自动化测试")

def init_report():
    cmd = "allure generate --clean report/html report/xml -o report/html"
    subprocess.call(cmd, shell=True)
    report_path ="/report/html/" + "index.html"
    logger.info("报告地址:{}".format(report_path))

if __name__ == "__main__":
    init_run_UI_Test()
    init_report()
