# -*- encoding: utf-8 -*-
'''
@File    :   handle_result.py
@Explain :   结果处理
@Data    :   2020/01/20 21:04:39
@Author  :   MdzzZ 
@Version :   1.0
'''

# here put the import lib
import os
import sys 
base_path = os.getcwd()
sys.path.append(base_path)

import json
from InterfaceTest.Util.handle_json import get_value
from deepdiff import DeepDiff

def handle_result(url, code):
    """
    针对返回结果，组合处理
    """
    # print("------->", code, "------->", type(code))
    data = get_value(url, "/Config/code_message.json")
    if data != None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None

def get_result_json(url, file_name=None):
    '''
    读取json中数据
    '''
    if file_name == None:
        file_path = base_path + '/InterfaceTest/Config/result.json'
    else:
        file_path = base_path + file_name
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
    return data[str(url)]

def handle_result_json(dict1, dict2):
    """
    校验格式
    """
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        # dict1 = {"aaa":"AAA", "bbb":"BBBB", "CC":[{"11":"22"}, {"11":"44"}]}
        # dict2 = {"c":"AAA", "bbb":"BBBB", "DDD":"D1", "ASD":[{"SSS":"111"}]}
        # dict3 = {"aaa":"123", "bbb":"456", "CC":[{"11":"111"}, {"11":"44"}]}
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        # print(cmp_dict)
        if cmp_dict.get("dictionary_item_added"):
            # print("case失败")
            return False
        else:
            # print("case通过")
            return True
    return False

if __name__ == "__main__":
    print(handle_result("App.User.Check", "1"))