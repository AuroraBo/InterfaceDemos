# -*- encoding: utf-8 -*-
'''
@File    :   run_main.py
@Explain :   统一执行用例
@Data    :   2020/01/20 19:26:56
@Author  :   MdzzZ 
@Version :   1.0
'''

# here put the import lib
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

import json
from InterfaceTest.Util.handle_header import get_header
from InterfaceTest.Util.handle_excel import excel_data
from InterfaceTest.Util.condition_data import get_data
from InterfaceTest.Util.handle_result import handle_result, handle_result_json, get_result_json
from InterfaceTest.Util.handle_cookie import get_cookie_value, write_cookie
from InterfaceTest.Base.base_requests import request

class RunMain():

    def run_main(self):
        """
        统一执行用例
        """     
        rows = excel_data.get_rows()
        for i in range(1, rows):
            cookie = None
            get_cookie = None
            header = None
            depend_data = None
            data = excel_data.get_rows_value(i+1)
            is_run = data[2]         
            if is_run == 'Y':
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
                if cookie_method == 'write':
                    """
                    必须是获取到cookie后写入
                    """
                    write_cookie(res, 'app')
                if is_header == 'yes':
                    header = get_header()
                res = request.run_main(method, url, data1, cookie, get_cookie, header)
                code = res['data']['err_code']
                message = res['msg']
                if except_method == 'mec':
                    config_message = handle_result(url, code)                
                    print("执行用例------>", data[1])
                    # print("message----->", message, "config_message------->", config_message)
                    # print("------->", res)
                    if message == config_message:
                        print("测试case通过")
                        excel_data.excel_write_data(i+1, 13, "通过")
                        excel_data.excel_write_data(i+1, 14, json.dumps(res))
                    else:
                        print("测试case失败")
                        excel_data.excel_write_data(i+1, 13, "失败")
                        excel_data.excel_write_data(i+1, 14, json.dumps(res))
                if except_method == 'errorcode':
                    print("执行用例------>", data[1])
                    # print("------->", res)
                    # print(type(except_result), type(code))
                    if except_result == code:
                        print("测试case通过")
                        excel_data.excel_write_data(i+1, 13, "通过")
                        excel_data.excel_write_data(i+1, 14, json.dumps(res))
                    else:
                        print("测试case失败")
                        excel_data.excel_write_data(i+1, 13, "失败")
                        excel_data.excel_write_data(i+1, 14, json.dumps(res))
                if except_method == 'json':
                    print("执行用例------>", data[1])
                    # print("------->", res)
                    really_result = get_result_json(url=url)
                    # print(really_result)
                    result = handle_result_json(res, really_result)
                    # print(result)
                    if result:
                        print("测试case通过")
                        excel_data.excel_write_data(i+1, 13, "通过")
                        excel_data.excel_write_data(i+1, 14, json.dumps(res))
                    else:
                        print("测试case失败")
                        excel_data.excel_write_data(i+1, 13, "失败")
                        excel_data.excel_write_data(i+1, 14, json.dumps(res))
            
if __name__ == "__main__":
    run = RunMain()
    run.run_main()