#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/10  4:23 下午
@Author  : Frank.lian
@File    : confighttp.py
@Description :重写post和get请求
'''
# !/usr/bin/env python3
# coding=utf-8
import urllib.parse, requests
from requests_toolbelt.utils import dump
from requests import ReadTimeout, RequestException
from common.getdata import GetData
from common.logger import Logger

req_session = requests.session()
logger = Logger(logger="ConfigHttp").getlog()


class ConfigHttp:

    def set_url(self, url):
        ''' 根据用户提供的项目名、端口号去判断项目的url拼接
        Args：
            url: String类型，接口相应的路径；
        '''
        self.url = GetData().get_url() + url

    def set_headers(self, headername=None, *args, **kwargs):
        ''' 设置请求头，录入系统名称和头类型
        Args：
            header：String类型，内容类型。json/text/空
        '''
        if headername == 'text':
            header = {"Content-Type": "text/plain"}
        elif headername == 'default':
            header = {"Content-Type": "application/json;charset=UTF-8"}
        elif headername == 'custom':
            header = {"Content-Type": "application/json;charset=UTF-8", "Accept-Encoding": "gzip, deflate, br","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
            for k, v in kwargs.items():
                header[k] = v
        else:
            header = GetData().get_token()
            header['Content-Type'] = "application/json;charset=UTF-8"
        self.header = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # 定义一个get请求
    def get(self):
        try:
            self.response = requests.get(self.url, params=self.params, headers=self.headers, timeout=60)
            logger.info('\n请求响应信息\n----------------------------------')
            dump_string = dump.dump_all(self.response).decode('utf-8')  # 获取所有的请求和相应数据，转换为String类型
            logger.info(urllib.parse.unquote(dump_string, encoding='utf-8'))  # 把String类型中的urldecode 转换成utf-8
            return self.response
        except ReadTimeout as t_error:
            # self.logger.error("Time out!")
            raise Exception(t_error)
        except RequestException as error:
            # self.logger.error(response.text)
            raise Exception(error)
        except ValueError as v_error:
            # self.logger.error(ValueError)
            raise Exception(v_error)
        except NameError as name_error:
            # self.logger.error(NameError)
            raise Exception(name_error)
        except AttributeError as attr_error:
            # self.logger.error(AttributeError)
            raise Exception(attr_error)
        finally:
            req_session.close()

    # 定义一个post请求
    def post(self):
        try:
            self.response = requests.post(self.url,  headers=self.header, data=self.data, timeout=30)
            logger.info('请求响应信息\n----------------------------------')
            dump_string=dump.dump_all(self.response).decode('utf-8')#获取所有的请求和相应数据，转换为String类型
            logger.info(urllib.parse.unquote(dump_string, encoding='utf-8'))#把String类型中的urldecode 转换成utf-8
            return self.response
        except ReadTimeout as t_error:
            raise Exception(t_error)
        except RequestException as error:
            raise Exception(error)
        except ValueError as v_error:
            raise Exception(v_error)
        except NameError as name_error:
            raise Exception(name_error)
        except AttributeError as attr_error:
            raise Exception(attr_error)
        finally:
            req_session.close()

    # 定义一个发送参数中包含文件的post请求
    def postWithFile(self):
        try:
            self.response = requests.post(self.url, headers=self.headers, files=self.files, timeout=30)
            logger.info('请求响应信息\n----------------------------------')
            dump_string = dump.dump_all(self.response).decode('utf-8')  # 获取所有的请求和相应数据，转换为String类型
            logger.info(urllib.parse.unquote(dump_string, encoding='utf-8'))  # 把String类型中的urldecode 转换成utf-8
            return self.response
        except ReadTimeout as t_error:
            raise Exception(t_error)
        except RequestException as error:
            raise Exception(error)
        except ValueError as v_error:
            raise Exception(v_error)
        except NameError as name_error:
            raise Exception(name_error)
        except AttributeError as attr_error:
            raise Exception(attr_error)
        finally:
            req_session.close()
