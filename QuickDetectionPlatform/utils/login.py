# -*- encoding: utf-8 -*-
"""
@File    : login.py
@Time    : 2022/6/17 15:57
@Author  : kui
@Software: PyCharm
"""
import requests
from common import config
from utils import Log
test_url = config.test_login_url
sta_url = config.sta_login_url
data = config.login_data
log = Log.Log.log
def login_test():
    """
    测试环境-登录
    :return: token
    """
    r = requests.post(url=test_url, json=data)
    token = r.json()['data']['token']
    log.info('本次登录获取token为:' + str({'Authorization': token}))
    return {'Authorization': token}


def login_sta():
    """
    预发布-登录
    :return: token
    """
    r = requests.post(url=sta_url, json=data)
    token = r.json()['data']['token']
    log.info('本次登录获取token为:' + str({'Authorization': token}))
    return {'Authorization': token}