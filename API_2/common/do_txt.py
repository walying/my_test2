# -*- coding: utf-8 -*-
# @Time     :2019/4/19  10:13
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :do_txt.py

from API_2.common import contants
"""
处理txt文件内容，并以列表的形式输出
"""
def file_analysis(file):
    with open(file) as test_file:  #读取test_0302文件
        resp = test_file.readlines()
        new_list=[]        #建立空列表
        for item in resp: #逐行读取
            item = item.strip("\n").split("@")   #清楚换行符，以“@”切分字符串
            new_dict = {}    #建立空字典
            for line in item:
                line = line.split(":" , 1)  #切分后的字符串再以第一个“：”继续切分
                new_dict[line[0]] = line[1]   # key：value 存入字典
            new_list.append(new_dict)         #每行结束后存入列表
        print(new_list)

file_analysis(contants.txt_file)