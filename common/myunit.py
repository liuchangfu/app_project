# _*_ coding:utf-8 _*_
import unittest
from common.desired_caps import start_app
from loguru import logger
import time
from common.common_fun import Common


class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = start_app()
        com = Common(self.driver)
        com.create_log('test_case_log')
        logger.info('=====setUp====')

    def tearDown(self):
        logger.info('====tearDown====')
        time.sleep(5)
        self.driver.close_app()
