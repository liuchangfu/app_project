# _*_ coding:utf-8 _*_
from BusinessView.loginview import LoginView
import unittest
from loguru import logger
from common.myunit import StartEnd


class TestLogin(StartEnd):

    def test_login_zxw2018(self):
        logger.info('============test_login_zxw2018=====')
        login = LoginView(self.driver)
        data = login.get_testcase_yaml('testcase.yaml')
        login.login_action(data['case1'][0]['username'], data['case1'][1]['password'])
        self.assertTrue(login.check_login_status())


if __name__ == '__main__':
    unittest.main()
