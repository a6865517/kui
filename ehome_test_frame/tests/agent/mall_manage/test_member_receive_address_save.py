# -*- encoding: utf-8 -*-
"""
@File    : test_member_receive_address_save.py
@Time    : 2022/7/19 10:07
@Author  : kui
@Software: PyCharm
"""
import allure
import pytest

from utils import read_yaml,request_main,base_assert


@pytest.mark.kui
@allure.story('商城添加地址')
@allure.title("{test_data[case]}")
@allure.link("http://jira.ehome.com/browse/PARTNER-384", name='jira地址')
@pytest.mark.parametrize('test_data', read_yaml.read_case(__file__))
def test_member_receive_address_save(test_data):
    res = request_main.request(test_data)
    base_assert.base_assert(res,test_data)
