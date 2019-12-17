# _*_ coding:utf-8 _*_
from BaseView.BaseView import BaseView
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.desired_caps import start_app
from loguru import logger
import datetime
import os
import yaml


class Common(BaseView):
    # 取消按钮定位器
    cancelBtn = (By.ID, 'android:id/button2')
    # 跳过按钮定位器
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')

    # 检查取消按钮
    def check_cancel_btn(self):
        logger.info('==========检查取消按钮=========')
        try:
            self.find_element(*self.cancelBtn).click()
        except NoSuchElementException:
            logger.info('未找到取消按钮')

    # 检查跳过按钮
    def check_skip_btn(self):
        logger.info('==========检查跳过按钮===========')
        try:
            self.find_element(*self.skipBtn).click()
        except NoSuchElementException:
            logger.info('未找到跳过按钮')

    # 获取手机屏幕大小
    def get_size(self):
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return x, y

    # 向左滑动
    def swipeLeft(self):
        logger.info('向左滑动')
        l = self.get_size()
        x1 = int(l[0] * 0.9)  # 起点x坐标
        y1 = int(l[1] * 0.5)  # y坐标
        x2 = int(l[0] * 0.1)  # 终点x坐标
        self.swipe(x1, y1, x2, y1, 1000)

    # 屏幕向上滑动
    def swipeUp(self):
        logger.info('向上滑动')
        l = self.get_size()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.swipe(x1, y1, x1, y2, 1000)

    # 屏幕向下滑动
    def swipeDown(self):
        logger.info('向下滑动')
        l = self.get_size()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.swipe(x1, y1, x1, y2, 1000)

    # 屏幕向右滑动
    def swipRight(self):
        logger.info('向右滑动')
        l = self.get_size()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.swipe(x1, y1, x2, y1, 100)

    # 获取当前时间，并按%Y-%m-%d-%H-%M-%S格式输出
    def get_time(self):
        now = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        return now

    # 截图
    def get_screenshot(self, module):
        time = self.get_time()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)
        logger.info('截图文件保存目录为:{}', image_file)
        self.driver.get_screenshot_as_file(image_file)

    # 生成日志文件
    def create_log(self, module):
        time = self.get_time()
        log_file = os.path.dirname(os.path.dirname(__file__)) + '/log/%s_%s.txt' % (module, time)
        logger.info(log_file)
        logger.add(log_file, format="{time:YYYY-MM-DD at HH:mm:ss}|{level}|{message}")

    # 读取yaml配置文件
    @staticmethod
    def get_testcase_yaml(file_name):
        dir1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', file_name)
        with open(dir1, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data

    @staticmethod
    def get_desired_list():
        dir2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'app.yaml')
        with open(dir2, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return data


if __name__ == '__main__':
    driver = start_app()
    com = Common(driver)
    # data = com.get_testcase_yaml()
    # print(data)
    # print(data['case1'])
    # print(data['case2'])
    # print(data['case1']['username'])
    # print(data['case1']['password'])
    # print(data['case2']['username'])
    # print(data['case2']['password'])
    # com.create_log('start app')
    # # com.check_cancel_btn()
    # # com.check_skip_btn()
    # time = com.get_time()
    # logger.info(time)
    # com.get_screenshot('start app')
