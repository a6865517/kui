# -*- coding:utf-8 -*-
"""
@Author: Leexzyy
@File:  run_test_interface_api.py
@CreateTime:  2021-06-10
@desc: 接口自动化系统入口
@APIURL:
"""
import os
import unittest
from datetime import datetime

from common import config
import get_path_info
from send_email import send_email_report
import requests

from my_beautiful_report import BeautifulReport as bf

# from my_beautiful_report

now = datetime.now()
folder_time_name = now.strftime('%Y-%m-%d')
report_time_name = now.strftime('%H-%M-%S')
folder_name = 'report/' + folder_time_name
report_root_path = ''
correct_rate = ''
case_fail = ''
report_dir = {'all_case': 0, 'case_success': 0, 'case_fail': 0, 'case_skip': 0, 'correct_rate': 0, 'case_time': 0}

print(folder_time_name)
print(report_time_name)
report_name = report_time_name + config.REPORT_NAME
path = get_path_info.get_path()
report_path = os.path.join(path, 'report', folder_time_name, report_name + '.html')


def create_report_folder():
    global report_root_path
    report_root_path = get_path_info.get_path() + '/' + folder_name
    os.makedirs(report_root_path, 0o777, exist_ok=True)


def run_interface_test_and_create_report():
    global correct_rate, case_fail
    # 存放测试用例文件夹
    test_dir = path + "/testCase"
    dis = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    runner = bf.BeautifulReport(dis)
    runner.report(
        description=config.REPORT_TITLE,
        report_dir='' + report_root_path,
        filename=report_name  # 生成测试报告的文件名
    )
    case_success = runner.success_count
    print('运行成功数量 == ' + str(case_success))
    fields = runner.fields
    print('fields === ' + str(fields))
    all_case = fields['testAll']
    case_fail = fields['testFail']
    case_time = fields['totalTime']
    case_skip = fields['testSkip']
    if case_fail == 0:
        correct_rate = 100
    else:
        fail_correct = case_fail / all_case
        correct_rate = 1 - fail_correct
        correct_rate = correct_rate * 100
        correct_rate = round(correct_rate, 2)

    print(f"一共运行{all_case}测试用例,成功{case_success}条,失败{case_fail}条,跳过{case_skip}条,成功率 {correct_rate}%,执行时间{case_time},")
    report_dir['all_case'] = all_case
    report_dir['case_success'] = case_success
    report_dir['case_fail'] = case_fail
    report_dir['case_skip'] = case_skip
    report_dir['correct_rate'] = correct_rate
    report_dir['case_time'] = case_time
    if config.EMAIL_ON_OFF == 'ON':
        bi_data = {
            'project_name': config.PROJECT_NAME,  # 填写项目名字
            'project_from': 0,  # CI/CD--0 平台 --1
            'project_type': 0,  # 接口--0 WEB --1 Android --2
            'pass_cases': case_success,  # 成功的用例数
            'fail_cases': case_fail  # 失败的用例数
        }
        requests.post(url='http://testbi.ehome.com/post_api_data', data=bi_data)
    else:
        print('调试模式 不发送埋点信息')


if __name__ == '__main__':
    create_report_folder()
    run_interface_test_and_create_report()
    if config.EMAIL_ON_OFF == 'ON':
        send_email_report.SendEmail().yagmail(report_path, report_dir)
    else:
        print('测试报告不发送 请查看config email_ON_OFF是否打开')
    if case_fail != 0:
        raise AssertionError('自动化接口测试错误！！请查看日志文件')
