# -*- encoding: utf-8 -*-
"""
@File    : unittestMain.py
@Time    : 2022/4/11 13:48
@Author  : kui
@Software: PyCharm
"""
import time
import unittest
from utils import log, my_utils
import requests

from common import config

api = config.api
headers = {'authorization': 'Basic aGVhbHRoLWFnZW50LWNsaWVudDpoZWFsdGgtYWdlbnQtY2xpZW50'}
time_name = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
code = time_name[2:4] + time_name[5:7] + time_name[8:10]
apis = 'http://test-client.ehomepoct.com/auth/mobile/token/sms?'


class UnittestMain(unittest.TestCase):
    """
    载入前后置
    """
    log = log.Log.log

    @classmethod
    def setUpClass(cls) -> None:
        print('开始执行用例，当前时间为： ' + time.strftime('%Y-%m-%d %H:%M:%S'))

    @classmethod
    def tearDownClass(cls) -> None:
        print('执行完毕，当前时间为： ' + time.strftime('%Y-%m-%d %H:%M:%S'))
        my_utils.del_test_data()  # 清除测试数据
        my_utils.del_test_code()  # 清除测试数据

    @staticmethod
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

    @staticmethod
    def req_request(methods='post', **kwargs):
        """
        接口传参
        """
        r = None
        url = api + kwargs['api']
        token = UnittestMain.get_token(kwargs['login_phone'])
        data = kwargs['data']
        if methods == 'post':
            r = requests.post(url, headers=token, json=data)
        elif methods == 'get':
            r = requests.get(url, headers=token, json=data)
        elif methods == 'put':
            r = requests.put(url, headers=token, json=data)
        if r is None:
            print('请求类型未声明')
        return r

    def req_assert(self, res, **kwargs) -> None:
        """
        通用断言
        """
        self.log.debug('本次执行的测试用例请求内容为：' + str(kwargs['data']))
        self.log.debug('本次执行的测试用例响应内容为：' + res.text)
        res_time = res.elapsed.total_seconds()
        self.assertLess(res_time, 1, '接口响应时间大于一秒')
        self.log.info('接口响应时间为：' + str(res_time))
        self.assertEqual(res.json()['busiCode'], kwargs['assert']['code'], 'busicode与预期不符')
        self.log.info('busicode与预期一致为：' + str(res.json()['busiCode']))
        self.assertEqual(res.json()['msg'], kwargs['assert']['msg'], 'msg与预期不符')
        self.log.info('msg与预期一致')

    def assert_data(self, r, **kwargs) -> None:
        """
        响应data断言
        assert_type：1为==断言，2为in断言
        """
        if kwargs['assert_type'] == 1:
            self.assertEqual(r.json()['data'], kwargs['assert']['data'], 'data内容与预期不符')
            self.log.info('响应内容与预期一致')
        elif kwargs['assert_type'] == 2:
            self.assertIn(str(kwargs['assert']['data']), str(r.json()['data']), 'data内容与预期不符')
            self.log.info('响应内容与预期一致')

    def assert_all(self, **kwargs) -> None:
        """
        合并断言
        """
        r = self.req_request(**kwargs)
        if r.status_code == 200:
            print(r.text)
            self.req_assert(r, **kwargs)
            self.assert_data(r, **kwargs)
        else:
            self.fail('接口请求失败,status_code非200')
