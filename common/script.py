# _*_ coding:utf-8 _*_
import yaml
import os


# file_name = 'testcase.yaml'
# dir1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', file_name)
# print(dir1)
#
# dict = yaml.load(open(dir1, 'r'), Loader=yaml.FullLoader)
# print(dict)
# print(dict['case1'])
# print(dict['case2'])
# print(dict['case1'][0]['username'])
# print(dict['case1'][1]['password'])
# print('==========================')
# print(dict['case2'][0]['username'])
# print(dict['case2'][1]['password'])

# with open('../config/app.yaml', 'r') as file:
#     data = yaml.load(file, Loader=yaml.FullLoader)
#
# print(data)
# print(data['ip'])
# print(data['ip'][0])
# print(data['ip'][1])


def get_desired_list():
    dir2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'app.yaml')
    with open(dir2, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data


data = get_desired_list()
print(data)
print(data['devices_list'])
print(data['devices_list'][0])
print(data['devices_list'][1])
