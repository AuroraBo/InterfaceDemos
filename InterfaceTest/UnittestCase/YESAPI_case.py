# -*- encoding: utf-8 -*-
'''
@File    :   YESAPI_case.py
@Explain :   YESAPI_case编写
@Data    :   2020/01/19 15:26:59
@Author  :   MdzzZ 
@Version :   1.0
'''

# here put the import lib
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

import json
import mock
import unittest
import HTMLTestRunnerMdzzZ
from InterfaceTest.Base.base_requests import request
def read_json():
    with open(base_path+'/InterfaceTest/Config/user_data.json', encoding='utf-8') as f:
        data = json.load(f) 
    return data

def get_value(key):
    data = read_json()
    return data[key]

host = 'http://hd215.api.yesapi.cn/?s='
class YESAPICase(unittest.TestCase):
    
    def test_login(self):
        url = host + 'App.User.LoginExt'
        data = {
            "app_key":"70F0E26AE7724CAE19E8062379C51728",
            "username":"h960107",
            "password":"h960107."
        }
        # mock_method = mock.Mock(return_value=get_value('LoginExt'))
        # request.run_main = mock_method
        res = request.run_main('post', url, data)
        # print(res)
        self.assertEqual(res['ret'], 200)
    
    def test_profile(self):
        url = host + 'App.User.Profile'
        data = {
            "app_key":"70F0E26AE7724CAE19E8062379C51728",
            "uuid":"86B8947D5A871400C9B3CC00505743CE",
            "token":"2FC996337A033C28B21828F008C40E2361917D00BC0755AE14A3AD47F14A0C72"
        }
        # mock_method = mock.Mock(return_value=get_value('Profile'))
        # request.run_main = mock_method
        res = request.run_main('post', url, data)
        # print(res)
        self.assertEqual(res['ret'], 200)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(YESAPICase('test_login'))
    suite.addTest(YESAPICase('test_profile'))
    file_path = base_path + '/InterfaceTest/Report/report.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunnerMdzzZ.HTMLTestRunner(stream=f, title="this is test", description="MdzzZ test")
        runner.run(suite)
    # unittest.main()