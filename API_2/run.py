# -*- coding: utf-8 -*-
# @Time     :2019/4/29  9:21
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :run.py.py
import sys
sys.path.append('./')#project根目录地址
print(sys.path)
import unittest
# from API_2.testcases import test_register_cases
# from API_2.testcases import test_login_cases
from API_2.common import contants
import HTMLTestRunnerNew

#方法一：
# suite=unittest.TestSuite()#收集器
# loader=unittest.TestLoader#加载器
#
# suite.addTests(loader.loadTestsFromModule(test_register_cases))
# suite.addTests(loader.loadTestsFromModule(test_login_cases))


#方法二：
discover=unittest.defaultTestLoader.discover(contants.case_dir,"test_*_cases.py")

with open(contants.report_dir+'/report.html','wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            title='Python15 API test report',
                                            description='前程贷API',
                                            tester="liying")
    runner.run(discover)


