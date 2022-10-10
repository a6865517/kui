# -*- encoding: utf-8 -*-
"""
@File    : read_yaml.py
@Time    : 2022/7/16 16:37
@Author  : kui
@Software: PyCharm
"""
import yaml


def read(path):
    """
    读取yaml文件
    :param path: 文件路径
    :return: results:文件内容
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    results = yaml.load(data, Loader=yaml.FullLoader)  # FullLoafer可以yaml解析变得安全
    return results


def read_case(names=str()):
    """
    测试用例读取yaml文件
    :return: results:文件内容
    """
    re = names.replace('tests', 'data')
    names = re.replace('.py', '.yaml')
    with open(names, 'r', encoding='utf-8') as f:
        data = f.read()
    results = yaml.load(data, Loader=yaml.FullLoader)  # FullLoafer可以yaml解析变得安全
    return results
