# -*- coding: utf-8 -*-
# @Time     :2019/4/17  11:02
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :test_login_cases.py


import unittest
import logging
from ddt import ddt,data,unpack
from API_2.common.do_excel import *
from API_2.common import http_request
from API_2.common import context
from API_2.common import contants
from API_2.common import do_mysql
from API_2.common import logger


@ddt
class LoginTest(unittest.TestCase):
    logger = logger.get_logger(__name__)
    @classmethod
    def setUpClass(cls):
        logger.get_logger(__name__).info('准备测试前置')
        cls.http_test=http_request.HTTPRequest2()
        cls.mysql=do_mysql.DoMysql()

    # def setUp(self):
    #     self.mysql = do_mysql.DoMysql()
    #读取测试用例
    do_Myexcel = DoExcel(contants.case_file, 'login')
    cases = do_Myexcel.get_cases()

    @data(*cases)#装饰方法
    def test_login(self,case):
        # 在请求之前替换参数化的值
        case.data = context.replace(case.data)
        print(case.data)

        self.logger.info('开始测试：{0}'.format(case.title))
        resp=self.http_test.request(case.method,case.url,case.data)
        #actual_code=resp.json()['code']
        try:
            #self.assertEqual(str(case.expected),actual_code)
            self.assertEqual(case.expected, resp.text)
            self.do_Myexcel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.do_Myexcel.write_result(case.case_id+1,resp.text,'FAIL')
            self.logger.error('报错了，{0}'.format(e))
            raise e

        self.logger.info('结束测试：{0}'.format(resp.text))
    @classmethod
    def tearDownClass(cls):
        logger.get_logger(__name__).info('准备测试后置')
        cls.http_test.close()
        cls.mysql.close()
        print("用例执行完毕")
    # def tearDown(self):
    #     self.mysql.close()