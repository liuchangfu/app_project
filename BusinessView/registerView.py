# _*_ coding:utf-8 _*_
from loguru import logger
from common.desired_caps import start_app
from selenium.webdriver.common.by import By
from common.common_fun import Common, NoSuchElementException
import random
import time


class RegisterView(Common):
    # 注册
    login_register = (By.ID, 'com.tal.kaoyan:id/login_register_text')
    # 头像设置相关元素
    userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    image = (By.ID, 'com.tal.kaoyan:id/iv_picture')
    save = (By.ID, 'com.tal.kaoyan:id/picture_tv_ok')
    menu_crop = (By.ID, 'com.tal.kaoyan:id/menu_crop')
    # 用户名密码邮箱相关元素
    register_username = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_btn = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')
    # 完善资料相关
    perfectinfomation_school = (By.ID, 'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    perfectinfomation_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    perfectinfomation_goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')
    # 院校相关元素
    forum_title = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    university_item_name = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')
    # 专业相关元素
    major_subject_title = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    major_group_title = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    major_search_item_name = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')
    # 我的
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    usercenter_username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

    def register_action(self, reg_username, reg_password, reg_email):
        self.check_cancel_btn()
        self.check_skip_btn()
        logger.info('=========正在注册========')
        self.find_element(*self.login_register).click()
        self.wait(2)
        logger.info('========选择头像===========')
        self.find_element(*self.userheader).click()
        self.find_elements(*self.image)[1].click()
        self.find_element(*self.save).click()
        self.find_element(*self.menu_crop).click()

        logger.info('输入的用户名:{}', reg_username)
        self.find_element(*self.register_username).send_keys(reg_username)
        time.sleep(3)
        logger.info('输入的的密码:{}', reg_password)
        self.find_element(*self.register_password).send_keys(reg_password)
        time.sleep(3)
        logger.info('输入的Email:{}', reg_email)
        self.find_element(*self.register_email).send_keys(reg_email)
        time.sleep(3)
        self.find_element(*self.register_btn).click()
        time.sleep(3)

        try:
            self.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            logger.error('注册失败！！')
            self.get_screenshot('register_fail')
            return False
        else:
            self.add_register_info()
            if self.check_register_status():
                return True
            else:
                return False

    def add_register_info(self):
        logger.info('=============选择学校===========')
        self.find_element(*self.perfectinfomation_school).click()
        self.find_elements(*self.forum_title)[2].click()
        self.find_elements(*self.university_item_name)[2].click()

        logger.info('=============选择专业===========')
        self.find_element(*self.perfectinfomation_major).click()
        self.find_elements(*self.major_subject_title)[2].click()
        self.find_elements(*self.major_group_title)[2].click()
        self.find_elements(*self.major_search_item_name)[2].click()

        self.find_element(*self.perfectinfomation_goBtn).click()

    def check_register_status(self):
        logger.info('=======检查注册登录用户名===========')
        try:
            self.find_element(*self.button_mysefl).click()
            self.find_element(*self.usercenter_username)
        except NoSuchElementException:
            logger.info('注册失败！！')
            self.get_screenshot('register_fail')
        else:
            reg_username = self.find_element(*self.usercenter_username).text
            logger.info('注册成功，你注册的用户名为:{}', reg_username)
            return True


if __name__ == '__main__':
    driver = start_app()
    com = Common(driver)
    com.create_log('register_action')
    register = RegisterView(driver)
    username = 'test' + str(random.randint(1000, 9000))
    password = 'liu' + str(random.randint(1000, 9000))
    email = 'change' + str(random.randint(1000, 9000)) + '@163.com'
    register.register_action(username, password, email)
