# -*- encoding: utf-8 -*-
"""
@File    : test_get_agent_info.py
@Time    : 2022/7/26 10:53
@Author  : kui
@Software: PyCharm
"""
import allure
import pytest

from utils import read_yaml,request_main,base_assert



@pytest.mark.kui
@allure.story('查询合伙人信息')
@allure.title("{test_data[case]}")
@allure.link("http://jira.ehome.com/browse/PARTNER-384", name='jira地址')
@pytest.mark.parametrize('test_data', read_yaml.read_case(__file__))
def test_member_receive_address_save(test_data):
    res = request_main.request(test_data)
    base_assert.base_assert(res,test_data)