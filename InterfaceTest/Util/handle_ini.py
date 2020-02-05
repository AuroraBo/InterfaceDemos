# -*- encoding: utf-8 -*-
'''
@File    :   handle_ini.py
@Explain :   ini文件读取
@Data    :   2020/01/20 19:45:56
@Author  :   MdzzZ 
@Version :   1.0
'''

# here put the import lib
import os
import sys 
base_path = os.getcwd()
sys.path.append(base_path)

import configparser

class HandIni(object):

    def load_ini(self):
        """
        加载ini文件
        """
        file_path = base_path + '/InterfaceTest/Config/server.ini'
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding='utf-8-sig')
        return cf

    def get_value(self, key, node=None):
        """
        获取ini文件内的value
        """
        if node == None:
            node = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(section=node, option=key)
        except Exception:
            print("没有获取到值")
            data = None
        return data

handle_ini = HandIni() 

if __name__ == "__main__":
    hi = HandIni()
    print(hi.get_value('host'))