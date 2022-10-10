# -*- encoding: utf-8 -*-
"""
@File    : request.py
@Time    : 2022/7/19 14:25
@Author  : kui
@Software: PyCharm
"""
import time
from utils import logger
import requests
from requests import sessions
from configparser import ConfigParser

log = logger.log

def __get_token(phone):
    """
    登录获取token
    :return:
    """
    apis = 'http://test-client.ehomepoct.com/auth/mobile/token/sms?'
    headers = {'authorization': 'Basic aGVhbHRoLWFnZW50LWNsaWVudDpoZWFsdGgtYWdlbnQtY2xpZW50'}
    time_name = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    code = time_name[2:4] + time_name[5:7] + time_name[8:10]
    path = f'code={code}&mobile={phone}&grant_type=mobile&scope=agent'
    url = apis + path
    r = requests.post(url, headers=headers)
    busiCode = r.json()['busiCode']
    if busiCode != 0:
        log.error(r.text)
    else:
        return {'authorization': r.json()['data']['token_type'] + ' ' + r.json()['data']['access_token']}


def request(*args, **kwargs):
    """
    封装request
    :param args:
    :param kwargs:
    :return:
    """
    HOST = None
    url = None
    headers = None
    method = 'POST'
    config = ConfigParser()
    config.read('./pytest.ini')
    config.read('../pytest.ini')
    config.read('../../../pytest.ini')
    if 'test' in str(config.get('pytest', 'addopts')):
        HOST = 'http://test-client.ehomepoct.com/'
    elif 'sta' in str(config.get('pytest', 'addopts')):
        HOST = 'http://sta-client-api.ehomepoct.com/'
    elif 'prod' in str(config.get('pytest', 'addopts')):
        HOST = 'http://client-c.ehomepoct.com/'
    else:
        log.error('HOST环境配置错误，请检查配置文件pytest.ini,addopts配置项')
    for i in args, kwargs:
        if i:
            method = i[0]['request']['methods']
            url = HOST + i[0]['request']['path']
            headers = __get_token(i[0]['request']['login_user'])
            if i[0]['request']['headers']:
                headers.update(i[0]['request']['headers'])
            log.info('本次请求请求头为:' + str(headers))
            log.info('本次请求请求参数为:' + str(i[0]['request']['data']))
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs, headers=headers)


if __name__ == '__main__':
    request()