# -*- encoding: utf-8 -*-
'''
@File    :   handle_header.py
@Explain :   header操作
@Data    :   2020/01/27 23:05:28
@Author  :   MdzzZ 
@Version :   1.0
'''

# here put the import lib
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

from InterfaceTest.Util.handle_json import read_json

def get_header():
    """
    获取json文件中header信息
    """
    data = read_json('/Config/header.json')
    return data

def header_md5():
    """
    header md5加密
    """
    data = get_header()
    data['imooc_key'] = 'md5加密'
    pass