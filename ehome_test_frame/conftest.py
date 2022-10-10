# -*- encoding: utf-8 -*-
"""
@File    : conftest.py.py
@Time    : 2022/7/21 16:21
@Author  : kui
@Software: PyCharm
"""
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="环境切换"
    )



