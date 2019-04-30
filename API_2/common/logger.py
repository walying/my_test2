# -*- coding: utf-8 -*-
# @Time     :2019/4/28  10:26
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :logger.py

import logging
from API_2.common import contants

def get_logger(name):
    #总开关，不同输出渠道还有各自的开关
    logger=logging.getLogger(name)
    logger.setLevel('DEBUG')

    fmt="%(asctime)s-%(name)s-%(filename)s-%(message)s-[%(filename)s:%(lineno)d]"
    formatter=logging.Formatter(fmt=fmt)

    #把日志级别放到配置文件里面配置--优化
    console_handler=logging.StreamHandler()#控制台
    console_handler.setLevel('DEBUG')
    console_handler.setFormatter(formatter)

    file_handler=logging.FileHandler(contants.log_dir+'/case15.log')
    file_handler.setLevel('INFO')
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


if __name__ == '__main__':
    logger=get_logger('')
    logger.info('测试开始啦')
    logger.error('测试报错')
    logger.debug('测试数据')
    logger.info('测试结束')