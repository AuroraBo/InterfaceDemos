# -*- encoding: utf-8 -*-
'''
@File    :   handle_cookie.py
@Explain :   cookie操作-获取/写入/携带cookie判断
@Data    :   2020/01/26 23:38:16
@Author  :   MdzzZ 
@Version :   1.0
'''

# here put the import lib
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

import json
from InterfaceTest.Util.handle_json import get_value, read_json, write_value

# 1、获取cookie
# 2、写入cookie
# 3、携带cookie操作

def get_cookie_value(cookie_key):
    """
    获取cookie值
    """
    data = read_json('/Config/cookie.json')
    return data[cookie_key]

def write_cookie(data, cookie_key):
    """
    写入cookie
    """
    data1 = read_json('/Config/cookie.json')
    data1[cookie_key] = data
    write_value(data1)

if __name__ == "__main__":
    data = {
        "aaaa":"111111111111111123"
    }
    write_cookie(data,'web')