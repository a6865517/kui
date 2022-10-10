# -*- coding:utf-8 -*-
"""
@Author: kui
@File:  my_utils.py
@CreateTime:  2021-10-08
"""
import ast

import requests
import yaml
import redis
from utils import mysql_res
import time

from common import config

time_name = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
api = config.api
code = time_name[2:4] + time_name[5:7] + time_name[8:10]
apis = 'http://test-client.ehomepoct.com/auth/mobile/token/sms?'
headers = {'authorization': 'Basic aGVhbHRoLWFnZW50LWNsaWVudDpoZWFsdGgtYWdlbnQtY2xpZW50'}


def open_yaml(path_yaml='../data/login.yaml'):
    """
    打开yaml文件
    """
    path = open(path_yaml, 'r', encoding="utf-8")
    login_yaml = yaml.load(path, Loader=yaml.FullLoader)
    return login_yaml


def get_token(phone):
    """
    登录获取token
    :return:
    """
    path = f'code={code}&mobile={phone}&grant_type=mobile&scope=agent'
    url = apis + path
    r = requests.post(url, headers=headers)
    busiCode = r.json()['busiCode']
    if busiCode != 0:
        print(r.json())
    else:
        return {'authorization': r.json()['data']['token_type'] + ' ' + r.json()['data']['access_token']}


def rediscur():
    """
    链接redis
    """
    pool = redis.ConnectionPool(host='172.16.47.3', port=32766, password='khrRjPuEwh', db=0,
                                decode_responses=True)
    rds = redis.Redis(connection_pool=pool)
    return rds


def del_test_data() -> None:
    """
    删除合伙人测试账号
    """
    sql = 'DELETE FROM term_agent WHERE phone = 13622221111'
    mysql_res.CreateEngine.update_sql(sql=sql)


def del_test_code(phone=13622221111) -> None:
    """
    删除redis验证码，避免发送频繁导致用例失败
    """
    rediscur().delete(f'sms:ehome-dist-crm-app:{phone}')


def send_register_code(phone=13622223661) -> None:
    """
    发送注册验证码
    """
    url = 'http://test-client.ehomepoct.com/ehome-dist-crm-app/app/center/agent/verifyCode/send'
    head = get_token(phone)
    data = {"phone": "13622221111", "smsType": "LOGIN"}
    requests.post(url, headers=head, json=data)


def get_register_code():
    """
    获取注册验证码
    """
    send_register_code()
    res = rediscur()
    data = res.get('sms:ehome-dist-crm-app:13622221111')
    res_code = ast.literal_eval(data)['code']
    return res_code


if __name__ == '__main__':
    del_test_code()
