# -*- encoding: utf-8 -*-
"""
@File    : conftest.py.py
@Time    : 2022/7/22 11:41
@Author  : kui
@Software: PyCharm
"""
import pytest
import requests

@pytest.fixture()
def send_phone_code_test():
    """
    发送手机验证码
    :return:
    """
    host = 'http://test-client.ehomepoct.com'
    url = host + '/health-agent-client/api/center/agent/verifyCode/send'
    data = {"phone": "13600006666","smsType": "APPREGISTACCOUNT"}
    res = requests.post(url,json=data)


if __name__ == '__main__':
    print(send_phone_code_test())

