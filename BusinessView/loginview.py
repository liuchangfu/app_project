# _*_ coding:utf-8 _*_
from loguru import logger
from common.desired_caps import start_app
from selenium.webdriver.common.by import By
from common.common_fun import Common, NoSuchElementException


class LoginView(Common):
    # 用户名输入框
    username = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    # 密码输入框
    password = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    # 登录按钮
    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    # 我的
    myselfBtn = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    # 登录成功后的用户名定位器
    login_username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    # 我的页面右上角齿轮按钮定位器
    rightBtn = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    # 个人设置退出按钮定位器
    loginout = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')
    # 退出按钮定位器
    commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    def login_action(self, username, password):

        self.check_cancel_btn()
        self.wait(3)
        self.check_skip_btn()
        self.wait(3)

        logger.info('=========登录========')
        logger.info('输入用户名:{}', username)
        self.wait(3)
        self.find_element(*self.username).send_keys(username)
        logger.info('输入密码:{}', password)
        self.driver.find_element(*self.password).send_keys(password)
        logger.info('======正在登录=======')
        self.find_element(*self.loginBtn).click()
        self.wait(3)
        logger.info('======登录成功=======')

    def check_login_status(self):
        logger.info('======检查登录用户名========')
        try:
            self.wait(3)
            self.find_element(*self.myselfBtn).click()
            self.find_element(*self.login_username)
        except NoSuchElementException:
            logger.error('登录失败')
            self.get_screenshot('login fail')
            return False
        else:
            username = self.find_element(*self.login_username).text
            logger.info('登录成功,登录的用户名：{}', username)
            self.login_out()
            return True

    def login_out(self):
        logger.info('=======检查退出========')
        try:
            self.wait(3)
            self.find_element(*self.rightBtn).click()
            self.wait(3)
            self.find_element(*self.loginout).click()
            self.wait(3)
            self.find_element(*self.commit).click()
            self.wait(3)
            logger.info('=======退出成功=========')
        except NoSuchElementException:
            logger.info('退出失败，页面元素不存在！！')


if __name__ == '__main__':
    driver = start_app()
    com = Common(driver)
    com.create_log('login_action')
    login = LoginView(driver)
    login.login_action('自学网2018', 'zxw2018')
    # login.login_action('自学网2018','34454')
    login.check_login_status()

