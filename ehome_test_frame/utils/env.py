# -*- encoding: utf-8 -*-
"""
@File    : env.py
@Time    : 2022/7/21 18:13
@Author  : kui
@Software: PyCharm
"""
from configparser import ConfigParser

from utils.logger import log


def env():
    """
    环境切换
    :return:
    """
    ENV = None
    config = ConfigParser()
    config.read('./pytest.ini')
    config.read('../pytest.ini')
    config.read('../../../pytest.ini')
    if 'test' in str(config.get('pytest', 'addopts')):
        ENV = 'test'
    elif 'sta' in str(config.get('pytest', 'addopts')):
        ENV = 'sta'
    elif 'prod' in str(config.get('pytest', 'addopts')):
        ENV = 'prod'
    else:
        log.error('HOST环境配置错误，请检查配置文件pytest.ini,addopts配置项')
    return ENV