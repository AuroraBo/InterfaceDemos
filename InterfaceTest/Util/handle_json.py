# -*- encoding: utf-8 -*-
'''
@File    :   handle_json.py
@Explain :   读取json文件中的内容
@Data    :   2020/01/20 20:51:09
@Author  :   MdzzZ 
@Version :   1.0
'''

# here put the import lib
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

import json

def read_json(file_name=None):
    """
    加载json文件
    """
    if file_name == None:
        file_path = base_path + '/InterfaceTest/Config/user_data.json'
    else:
        file_path = base_path + '/InterfaceTest' + file_name
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f) 
    return data

def get_value(key, file_name=None):
    """
    获取json文件中的内容
    """
    data = read_json(file_name)
    return data.get(key)
    # return data[key]

def write_value(data):
    """
    写入json数据
    """
    data_value = json.dumps(data)
    with open(base_path+'/InterfaceTest/Config/cookie.json', "w") as f:
        f.write(data_value)

if __name__ == "__main__":
    data = {
        "aaaa":"bbbbbbb"
    }
    write_value(data)