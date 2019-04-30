# -*- coding: utf-8 -*-
# @Time     :2019/4/17  9:59
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :contants.py

import os

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

case_file=os.path.join(base_dir,'data','testcase.xlsx')
print(case_file)

txt_file=os.path.join(base_dir,'data','test.txt')
print(txt_file)

global_file=os.path.join(base_dir,'config','global.cfg')
print(global_file)

online_file=os.path.join(base_dir,'config','online.cfg')
print(online_file)

test_file=os.path.join(base_dir,'config','test.cfg')
print(test_file)

loglevel_file=os.path.join(base_dir,'config','log_level.cfg')
print(loglevel_file)

log_dir=os.path.join(base_dir,'log')

case_dir=os.path.join(base_dir,'testcases')

report_dir=os.path.join(base_dir,'reports')