# -*- encoding: utf-8 -*-
'''
@File    :   condition_data.py
@Explain :   数据以来处理
@Data    :   2020/01/29 19:28:22
@Author  :   MdzzZ 
@Version :   1.0
'''

# here put the import lib
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

from InterfaceTest.Util.handle_excel import excel_data
from jsonpath_rw import parse
import json

def split_data(data):
    """
    分割依赖条件
    """
    case_id = data.split(">")[0]
    # case_id_list = case_id.split("/")
    rule_data = data.split(">")[1]
    # rule_data_list = rule_data.split("/")
    return case_id, rule_data

def depend_data(data):
    """
    获取依赖结果集
    """
    # case_id_list = split_data(data)[0]
    # a = []
    # for case_id in case_id_list:
    #     row_number = excel_data.get_rows_number(case_id)
    #     data = excel_data.get_cell_value(row_number, 14)
    #     a.append(data)
    # return a
    case_id = split_data(data)[0]
    row_number = excel_data.get_rows_number(case_id)
    data = excel_data.get_cell_value(row_number,14)
    return data

def get_depend_data(res_data, key):
    """
    获取依赖字段
    """ 
    # res_data = json.loads(res_data)
    # key = split_data(key)[1]
    # # print(key)
    # a = []
    # for i in key:
    #     # print(i)
    #     json_exe = parse(i)
    #     madle = json_exe.find(res_data)
    #     a.append([math.value for math in madle][0])
    # return a
    # print(madle)
    # return [math.value for math in madle][0]
    # for math in madle:
    #     return math.value

    res_data = json.loads(res_data)
    json_exe = parse(key)
    madle = json_exe.find(res_data)
    return [math.value for math in madle][0]

def get_data(data):
    """
    获取依赖数据
    """
    res_data = depend_data(data)
    rule_data = split_data(data)[1]
    return get_depend_data(res_data,rule_data)

if __name__ == "__main__":
    data = {
                "ret": 200, "data": 
                {
                    "err_code": 0, "err_msg": "", "uuid": "86B8947D5A871400C9B3CC00505743CE", 
                    "token": "ADEA7EF441B886B3D440680A4929A1AE348E9961F401D068FEA7CEB5E44D1FD2", 
                    "role": "admin"
                }, 
                "msg": "V1.4.12 \u5c0f\u767d\u5f00\u653e\u63a5\u53e3 App.User.LoginExt"
            }
    key = 'YESAPI_001>data.uuid/data.token'
    print(get_depend_data(data, key))