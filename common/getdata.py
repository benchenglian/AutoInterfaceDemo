#!/usr/bin/env python
# -*- coding: utf-8 -*-


import codecs
import configparser
import json
import random
import string
import time
import os

config = configparser.ConfigParser()
proDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
'''
@Time    : 2021/12/10  4:24 下午
@Author  : Frank.lian
@File    : getdata.py
@Description :获取请求url和json文件内容
'''


class GetData(object):

    # 获取请求url
    def get_url(self):
        configPath = proDir + '/testfiles/config_file/config.ini'
        path = os.path.abspath(configPath)
        config.read(path, encoding="utf-8")
        url = config.get('testServer', 'url')
        return url

    # 获取config.ini中的username
    def get_username(self):
        configPath = proDir + '/testfiles/config_file/config.ini'
        path = os.path.abspath(configPath)
        config.read(path, encoding="utf-8")
        username = config.get('testServer', 'username')
        return username

    def get_token(self):
        """
        获取请求token
        """
        configPath = proDir + '/testfiles/config_file/config.ini'
        path = os.path.abspath(configPath)
        config.read(path, encoding="utf-8")
        token = config.get('Token', 'token')
        cookie = config.get('Cookie', 'cookie')
        return {"token": token, "Cookie": cookie}

    def read_json_file(self, filename):
        """ 读取json文件,返回的是字典
        Args：
            filename: String类型，文件名称；/testfiles/json_data/路径下文件
        return:
            返回json结构数据
        """
        json_fi = codecs.open(proDir + '/testfiles/json_data/' + filename, 'r', encoding='UTF-8')
        json_content = json_fi.read()
        json_fi.close()
        return json.loads(json_content.encode('UTF-8'))

    # def read_yaml_file(self,filename):
    #     """ 读取yaml文件
    #     Args：
    #         filename: String类型，文件名称；/testfiles/json_data/路径下文件
    #     return:
    #         返回json结构数据
    #     """
    #     yaml_fi = codecs.open(proDir+'/testfiles/json_data/'+filename,'r',encoding='utf-8')
    #     yaml_content = yaml_fi.read()
    #     yaml_fi.close()
    #     return yaml.load(yaml_content.encode('utf-8'),yaml.FullLoader)

    def read_schema_file(self, filename):
        """ 读取schema文件,返回的是字典
        Args：
            filename：String类型，文件名称；/testfiles/schema_file/路径下文件。
        return:
            返回json结构数据
        """
        json_fi = codecs.open(proDir + '/testfiles/schema_file/' + filename, 'r', encoding='UTF-8')
        json_content = json_fi.read()
        json_fi.close()
        return json.loads(json_content.encode('UTF-8'))

    def get_time(self):
        """获取当前时间
        return: 返回当前系统时间
        """
        return time.strftime("%m%d%H%M%S", time.localtime())

    def get_filePath(self, filename):
        """ 上传数据用，支持单文件和多文件
        Args：
            filename：文件名称，单个文件为String类型，多个文件为list列表；/testfiles/upload_file/路径下文件。
        return:
            单个文件，返回字典{"file":binary}
            多个文件，返回list包含元组[("file":binary),("file":binary)]
        """
        if type(filename) is str:  # 判断传参是否为字符串
            # 获取当前脚本所在路径的上层路径，并拼接"test_file"
            file = open(proDir + '/testfiles/upload_file/' + filename, "rb")
            return {"file": file}
        if type(filename) is list:  # 判断传参是否为列表
            multiple_files = []
            for num in range(0, len(filename)):
                files = ('file', open(proDir + '/testfiles/upload_file/' + filename[num], "rb"))
                multiple_files.append(files)
            return multiple_files
