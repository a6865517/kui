# -*- encoding: utf-8 -*-
"""
@File    : logger.py
@Time    : 2022/7/18 9:07
@Author  : kui
@Software: PyCharm
"""
import loguru, time, os

log = loguru.logger

t = time.strftime("%Y-%m-%d") # 获取当前时间

time_name = time.strftime('%H：%M：%S')

_log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/logs/' + t

log.add(f"{_log_path}.log", encoding="utf-8",rotation="200 MB")

