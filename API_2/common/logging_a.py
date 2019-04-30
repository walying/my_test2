# -*- coding: utf-8 -*-
# @Time     :2019/4/19  10:47
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :logging_a.py

#写一个日志类
#结合配置文件 完成 输出的格式 输出的级别的配置

import logging
import os
from API_2.common import config_a
from API_2.common import contants

class myLog:
    def __init__(self,fmt_out,level_in,level_out):
        self.fmt_out=fmt_out
        self.level_in=level_in
        self.level_out=level_out
    def log_msg(self):
        fmt_out= logging.Formatter(self.fmt_out)
        # 新建指定的输出渠道：
        my_logger = logging.getLogger('py15')  # 名为py15的日志收集器
        my_logger.setLevel(self.level_in)  # 设定收集的级别

        # # 1)指定输出渠道
        ch = logging.StreamHandler()  # 指定输出到console控制台
        ch.setLevel(level_out)  # 设定输出信息的级别
        ch.setFormatter(fmt_out)

        # 2)指定输出到.log文件
        log_file = os.path.join(contants.base_dir, 'log', 'common.log')
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(self.level_out)
        file_handler.setFormatter(fmt_out)

        # 配合关系
        my_logger.addHandler(ch)
        my_logger.addHandler(file_handler)
        # 收集日志
        my_logger.debug('this is debug msg')
        my_logger.info('this is info msg')
        my_logger.warning('this is warning msg')
        my_logger.error('this is error msg')
        my_logger.critical('this is critical msg')

if __name__ == '__main__':
    level_in=config_a.myConfig(contants.loglevel_file).get_strValue('LEVELIN', 'level_in')
    #print(level_in)
    level_out = config_a.myConfig(contants.loglevel_file).get_strValue('LEVELOUT', 'level_out')
    #print(level_out)
    fmt_out=config_a.myConfig(contants.loglevel_file).get_strValue('FMT', 'fmt')
    #print(fmt_out)
    myLog(fmt_out,level_in,level_out).log_msg()