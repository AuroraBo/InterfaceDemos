# -*- encoding: utf-8 -*-
'''
@File    :   stu_ddt.py
@Explain :   ddt学习
@Data    :   2020/01/30 17:43:18
@Author  :   MdzzZ 
@Version :   1.0
'''

# here put the import lib
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

import ddt
import unittest
from InterfaceTest.Util.handle_excel import excel_data
data = excel_data.get_excel_data()

# data = [[1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7], [4,5,6,7,8]]
@ddt.ddt
class TestCase01(unittest.TestCase):

    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case执行结束")

    @ddt.data(*data)
    def test_01(self, data1):
        # case_number	function	是否执行	precondition	依赖key	url	method	data	
        # cookie操作	header操作	预期结果方式	预期结果	结果	数据
        case_id, function, is_run, precondition, depend, url, method, request_data, cookie, header, except_method, except_res, result, result_data = data1
        # casename, casenum, isrun, method, cookie = data1
        print("this is test case",case_id, function, is_run, precondition, depend, url, method, request_data, cookie, header, except_method, except_res, result, result_data)

if __name__ == "__main__":
    unittest.main()