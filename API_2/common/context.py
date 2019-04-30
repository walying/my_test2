# -*- coding: utf-8 -*-
# @Time     :2019/4/23  11:25
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :context.py

import re
from API_2.common import config
import configparser

class Context:
    loan_id=None

def replace(data):
    p = '#(.*?)#'  # 正则表达式
    while re.search(p, data):
        m = re.search(p, data)  # 从任意位置开始找，找第一个就返回match object，否则返回None
        #print(m)
        #print(m.group(0))  # 返回表达式和组里面的内容
        #print(m.group(1))  # 只返回指定组的内容
        g = m.group(1)  # 拿到参数化的key
        try:
            v = config.ReadConfig().get('data', g)  # 根据key取配置文件里的值
            print(v)
        except configparser.NoOptionError as e:#如果配置文件里没有的话，去Context找
            if hasattr(Context,g):
               v=getattr(Context,g)
            else:
                print('找不到参数化的值')
                raise e

        #记得替换后的内容，继续用data接收
        data = re.sub(p, v, data, count=1)  # 查找替换
        print(data)
    return data

if __name__ == '__main__':

    data='{"mobilephone":"#admin_user#","pwd":"#admin_pwd#"}'
    replace(data)