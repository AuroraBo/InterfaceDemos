# -*- encoding: utf-8 -*-
'''
@File    :   base_requests.py
@Explain :   封装request-post/get
@Data    :   2020/01/19 15:08:56
@Author  :   MdzzZ 
@Version :   1.0
'''

# here put the import lib
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

import requests
import json
from InterfaceTest.Util.handle_ini import handle_ini
from InterfaceTest.Util.handle_json import get_value
from InterfaceTest.Util.handle_cookie import write_cookie

class BaseRequest(object):

    def send_post(self, url, data, cookie=None, get_cookie=None, header=None):
        """
        发送post请求
        """
        response = requests.post(url=url, data=data, cookies=cookie, headers=header)
        if get_cookie != None:
            """
            get_cookie = {"is_cookie":"app"}
            """
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    def send_get(self, url, data, cookie=None, get_cookie=None, header=None):
        """
        发送get请求
        """
        response = requests.get(url=url, params=data, cookies=cookie, headers=header)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    def run_main(self, method, url, data, cookie=None, get_cookie=None, header=None):
        """
        执行方法, 传递method/url/data
        """
        # return get_value(url)
        base_url = handle_ini.get_value('host')
        if 'http' not in url:
            url = base_url + url
        if method == 'get':
            res = self.send_get(url, data, cookie, get_cookie, header)
        elif method == 'post':
            res = self.send_post(url, data, cookie, get_cookie, header)
        else:
            raise ValueError
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        # print("------->",res)
        return res

request = BaseRequest()

if __name__ == "__main__":
    request = BaseRequest()
    data = {
        "app_key":"70F0E26AE7724CAE19E8062379C51728",
        "username":"h960107",
        "password":"h960107."
    }
    print(request.run_main('post', url='App.User.LoginExt', data=data))