# _*_ coding:utf-8 _*_
import unittest
from BSTestRunner import BSTestRunner
import time
from loguru import logger
import sys
import os
dir = os.path.abspath(os.pardir)
logger.info(dir)
sys.path.append(dir)


test_case_dir = dir + '/test_case'
logger.info('测试用例的路径为:{}', test_case_dir)
report_dir = dir + '/reports/'
logger.info('测试报告的路径为:{}', report_dir)

discover = unittest.defaultTestLoader.discover(test_case_dir, pattern='test_login.py')
now = time.strftime('%Y-%m-%d_%H_%M_%S')
report_name = report_dir + now + '_test_report.html'

with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='Kyb Test Report', description='kyb Android app test report')
    logger.info('正在执行测试用例...')
    runner.run(discover)
