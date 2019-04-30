# -*- coding: utf-8 -*-
# @Time     :2019/4/25  13:50
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :test_invest_cases.py

import unittest
from ddt import ddt,data
from API_2.common.do_excel import *
from API_2.common import http_request
from API_2.common import config
from API_2.common import contants
from API_2.common import do_mysql
from API_2.common import context
from API_2.common.context import Context
from API_2.common import logger

@ddt
class investTest(unittest.TestCase):
    logger = logger.get_logger(__name__)
    @classmethod
    def setUpClass(cls):
        logger.get_logger(__name__).info('准备测试前置')
        cls.http_test=http_request.HTTPRequest2()
        cls.mysql = do_mysql.DoMysql()

    #读取测试用例
    do_Myexcel = DoExcel(contants.case_file, 'invest')
    cases = do_Myexcel.get_cases()

    @data(*cases)  # 装饰方法
    def test_invest(self, case):
        self.logger.info('开始测试:{0}'.format(case.title))
        # 在请求之前替换参数化的值
        case.data = context.replace(case.data)
        resp = self.http_test.request(case.method, case.url, case.data)
        actual_code=resp.json()['code']
        try:
            self.assertEqual(str(case.expected),actual_code)
            #self.assertEqual(case.expected, resp.text)
            self.do_Myexcel.write_result(case.case_id + 1, resp.text, 'PASS')
            #判断加标成功之后，查询数据库，取到Loan_id
            if resp.json()['msg']=='加标成功':
                sql='SELECT id FROM future.loan WHERE memberid=1008 ORDER BY id DESC LIMIT 1'
                loan_id=self.mysql.fetch_one(sql)['id']
                print('标的ID',loan_id)
                #保存到类属性里面
                setattr(Context,'loan_id',str(loan_id))
        except AssertionError as e:
            self.do_Myexcel.write_result(case.case_id + 1, resp.text, 'FAIL')
            self.logger.error('报错了，{0}'.format(e))
            raise e
        self.logger.info('结束测试：{0}'.format(resp.text))

    @classmethod  # 所有的用例执行完之后才会执行此类方法
    def tearDownClass(cls):
        logger.get_logger(__name__).info('准备测试后置')
        cls.http_test.close()
        cls.mysql.close()
        print("用例执行完毕")
