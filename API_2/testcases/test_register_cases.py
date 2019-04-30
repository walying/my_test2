# -*- coding: utf-8 -*-
# @Time     :2019/4/22  14:19
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :test_register_cases.py

import unittest
from ddt import ddt,data,unpack
from API_2.common.do_excel import *
from API_2.common import http_request
from API_2.common import config
from API_2.common import contants
from API_2.common import do_mysql
from API_2.common import logger
import random

@ddt
class RegisterTest(unittest.TestCase):
    logger=logger.get_logger(__name__)
    @classmethod
    def setUpClass(cls):
        cls.http_test=http_request.HTTPRequest2()
        cls.mysql=do_mysql.DoMysql()
        logger.get_logger(__name__).info('准备测试前置')


    #读取测试用例
    do_Myexcel = DoExcel(contants.case_file, 'register')
    cases = do_Myexcel.get_cases()

    @data(*cases)#装饰方法
    def test_register(self,case):
        #print(case.data.find('register_mobile'))
        self.logger.info('开始测试：{0}'.format(case.title))
        i = random.randint(20, 100)
        if case.data.find('register_mobile') > -1:
            sql='select max(mobilephone) from future.member'
            max_phone=self.mysql.fetch_one(sql)['max(mobilephone)']#查询最大手机号码
            #最大手机号码-i
            max_phone=int(max_phone)-i
            print(max_phone)
            #replace方法是转换之后重新返回一个新的字符串
            case.data=case.data.replace('register_mobile',str(max_phone))

        resp=self.http_test.request(case.method,case.url,case.data)
        #print(resp.text)
        #actual_code=resp.json()['code']
        try:
            #self.assertEqual(str(case.expected),actual_code)
            self.assertEqual(case.expected, resp.text)
            self.do_Myexcel.write_result(case.case_id+1,resp.text,'PASS')
            #数据库校验，查询数据库是否存在刚注册手机号
            if resp.json()['msg']=='注册成功':
                sql='SELECT * FROM future.member WHERE mobilephone='+str(max_phone)
                member_id=self.mysql.fetch_one(sql)['mobilephone']
                print(member_id)
                self.assertEqual(member_id,str(max_phone))
        except AssertionError as e:
            self.do_Myexcel.write_result(case.case_id+1,resp.text,'FAIL')
            self.logger.info('报错了,{0}'.format(e))
            raise e
        self.logger.info('结束测试：{0}'.format(resp.text))

    @classmethod
    def tearDownClass(cls):
        cls.http_test.close()
        cls.mysql.close()
        logger.get_logger(__name__).info('准备测试后置')
        print("用例执行完毕")


    # def tearDown(self):
    #     self.mysql.close()