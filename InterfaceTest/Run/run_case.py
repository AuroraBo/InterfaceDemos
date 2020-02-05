# -*- encoding: utf-8 -*-
'''
@File    :   run_case.py
@Explain :   数据驱动执行case
@Data    :   2020/01/30 18:05:18
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
import json
import HTMLTestRunnerMdzzZ
from InterfaceTest.Util.handle_header import get_header
from InterfaceTest.Util.handle_excel import excel_data
from InterfaceTest.Util.condition_data import get_data
from InterfaceTest.Util.handle_result import handle_result, handle_result_json, get_result_json
from InterfaceTest.Util.handle_cookie import get_cookie_value, write_cookie
from InterfaceTest.Base.base_requests import request
data = excel_data.get_excel_data()

@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):
    
    @ddt.data(*data) 
    def test_main_case(self, data):
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        # data = excel_data.get_rows_value(i+1)
        is_run = data[2]  
        case_id = data[0] 
        i = excel_data.get_rows_number(case_id)      
        if is_run == 'Y':
            try:
                method = data[6]
                url = data[5]
                data1 = json.loads(data[7])
                is_header = data[9]
                except_method = data[10]
                except_result = data[11]
                condition = data[3]
                if condition:
                    """
                    获取依赖数据
                    """
                    depend_key = data[4]
                    depend_data = get_data(condition)
                    data1[depend_key] = depend_data
                    # print(data1)
                cookie_method = data[8]
                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    """
                    必须是获取到cookie后写入
                    """
                    get_cookie = {"is_cookie":"app"}               
                # if cookie_method == 'write':
                #     """
                #     必须是获取到cookie后写入
                #     """
                #     write_cookie(res, 'app')
                if is_header == 'yes':
                    header = get_header()
                res = request.run_main(method, url, data1, cookie, get_cookie, header)
                code = res['data']['err_code']
                message = res['msg']
                if except_method == 'mec':
                    config_message = handle_result(url, code)   
                    """             
                    # print("执行用例------>", data[1])
                    # print("message----->", message, "config_message------->", config_message)
                    # print("------->", res)
                    if message == config_message:
                        # print("测试case通过")
                        excel_data.excel_write_data(i, 13, "通过")
                        excel_data.excel_write_data(i, 14, json.dumps(res))
                    else:
                        # print("测试case失败")
                        excel_data.excel_write_data(i, 13, "失败")
                        excel_data.excel_write_data(i, 14, json.dumps(res))
                    """
                    try:
                        self.assertEqual(message, config_message)
                        excel_data.excel_write_data(i, 13, "通过")
                    except Exception:
                        excel_data.excel_write_data(i, 13, "失败")
                        raise Exception
                    else:
                        excel_data.excel_write_data(i, 14, json.dumps(res))

                if except_method == 'errorcode':
                    """
                    # print("执行用例------>", data[1])
                    # print("------->", res)
                    # print(type(except_result), type(code))
                    if except_result == code:
                        # print("测试case通过")
                        excel_data.excel_write_data(i, 13, "通过")
                        excel_data.excel_write_data(i, 14, json.dumps(res))
                    else:
                        # print("测试case失败")
                        excel_data.excel_write_data(i, 13, "失败")
                        excel_data.excel_write_data(i, 14, json.dumps(res))
                    """
                    try:
                        self.assertEqual(except_result, code)
                        excel_data.excel_write_data(i, 13, "通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "失败")
                        raise e
                    else:
                        excel_data.excel_write_data(i, 14, json.dumps(res))

                if except_method == 'json':
                    """
                    # print("执行用例------>", data[1])
                    # print("------->", res)
                    really_result = get_result_json(url=url)
                    # print(really_result)
                    result = handle_result_json(res, really_result)
                    # print(result)
                    if result:
                        # print("测试case通过")
                        excel_data.excel_write_data(i, 13, "通过")
                        excel_data.excel_write_data(i, 14, json.dumps(res))
                    else:
                        # print("测试case失败")
                        excel_data.excel_write_data(i, 13, "失败")
                        excel_data.excel_write_data(i, 14, json.dumps(res))
                    """
                    try:
                        self.assertTrue(except_method)
                        excel_data.excel_write_data(i, 13, "通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "失败")
                        raise e
                    else:
                        excel_data.excel_write_data(i, 14, json.dumps(res))
            except Exception as e:
                excel_data.excel_write_data(i, 13, "失败")
                raise e
        else:
            excel_data.excel_write_data(i, 13, "未执行")

if __name__ == "__main__":
    case_path = base_path+"/InterfaceTest/Run"
    report_path = base_path+"/InterfaceTest/Report/report.html"
    discover = unittest.defaultTestLoader.discover(case_path,pattern="run_case*.py")
    #unittest.TextTestRunner().run(discover)
    with open(report_path,"wb") as f:
        runner = HTMLTestRunnerMdzzZ.HTMLTestRunner(stream=f,title="MdzzZ",description="this is test")
        runner.run(discover)