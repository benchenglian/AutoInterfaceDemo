#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/10  4:46 下午
@Author  : Frank.lian
@File    : test_search.py
@Description : 测试查询接口
'''
import json

import allure
import pytest
from model.search import Search


class Test_search(object):

    search_parameters = [("接口自动化", "从原理到实战，带你进阶接口测试"),
                         ("python自动化", "快速上手Python，让重复工作自动化")]

    @allure.story("查询模块")
    @pytest.mark.parametrize("keyword,expect", search_parameters)
    def test_serv_search(self, keyword, expect):
        r_data = Search().serv_search_associate(keyword)
        assert r_data.status_code == 200
        assert r_data.json()['data']['list'][0]['product']['subtitle'] == expect
