# _*_ coding:utf-8 _*_
from appium import webdriver
from loguru import logger
import yaml
import os
import datetime
import multiprocessing

# app启动配置
with open('..\\config\\app.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# 手机设备
devices_list = ['127.0.0.1:62026', '127.0.0.1:62025']


def start_app(ip='http://127.0.0.1:4723/wd/hub', udid='127.0.0.1:62026'):
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid
    app_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', data['app_name'])
    desired_caps['app'] = app_path
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['automationName'] = data['automationName']
    desired_caps['noReset'] = data['noReset']
    logger.info('appium服务正在启动,运行端口为：{},运行机器为：{} at {}', ip, udid, datetime.datetime.now())
    driver = webdriver.Remote(ip, desired_caps)
    driver.implicitly_wait(5)
    return driver


desired_process = []

for i in range(len(devices_list)):
    port = 4723 + 2 * i
    desired = multiprocessing.Process(target=start_app, args=(data['ip'][i], devices_list[i]))
    desired_process.append(desired)

if __name__ == '__main__':
    # start_app('http://127.0.0.1:4723/wd/hub', devices_list[0])
    # start_app(data['ip'][0], devices_list[0])
    # start_app(data['ip'][1], devices_list[1])
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()
