#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import urllib
from common import confighttp
from common.getdata import GetData

'''
@Time    : 2021/12/10  4:38 下午
@Author  : Frank.lian
@File    : search.py
@Description : 查询
'''
# 登录url
serv_search_url = '/serv/v3/search'
# 列表json
cf = confighttp.ConfigHttp()
search_json = GetData().read_json_file("search.json")


class Search(object):

    def serv_search_associate(self, keyword):
        """
        查询模块接口-未登录；
        :param keyword: int类型 设置秒
        :return: 返回查询接口response
        """
        search_json['keyword'] = keyword
        cf.set_url(serv_search_url)
        cf.set_data(json.dumps(search_json, ensure_ascii=False, indent=4).encode("utf-8"))
        cf.set_headers('custom', Referer="https://time.geekbang.org/search?" + "q=" + urllib.parse.quote(
            keyword) + "&category=product",
                       Cookie="gksskpitn=aed6dc57-b353-4cf6-9b5f-422f90b22b15; _ga=GA1.2.1117236880.1638517903; LF_ID=1638517903066-2571171-584434; GCID=9213dad-4f935e0-e54fa72-83e54ba; GRID=9213dad-4f935e0-e54fa72-83e54ba; Hm_lvt_59c4ff31a9ee6263811b23eb921a5083=1638511920,1638517903,1638517928,1639124067; _gid=GA1.2.580375583.1639124067; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217da3689cdfb9a-03ea5ae6f20789-1632685d-2073600-17da3689ce0f23%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Ftime.geekbang.org%2F%22%7D%2C%22%24device_id%22%3A%2217d7f470e407ae-0df45f0524c8c9-1632685d-2073600-17d7f470e41e1e%22%7D; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1638517903,1638517928,1639124067,1639124082; Hm_lpvt_59c4ff31a9ee6263811b23eb921a5083=1639125256; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1639125256; gk_process_ev={%22count%22:12%2C%22utime%22:1639124081884%2C%22target%22:%22%22}; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1639127263|1639124066; _gat=1", )
        return cf.post()
