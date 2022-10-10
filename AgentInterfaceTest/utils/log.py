# -*- coding:utf-8 -*-
"""
@Author: kui
@File:  log.py
@CreateTime:  2021-09-29
@desc: 基于logger进行日志模块封装
"""
import os
import time

import loguru

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Log:
    """
    log日志类
    可通过log().log使用logger类里的方法
    """
    log = loguru.logger
    # 获取当前时间
    t = time.strftime("%Y-%m-%d")
    time_name = time.strftime('%H：%M：%S')
    log_path = path + '/logs/' + t
    log.add(f"{log_path}/{time_name}.log", encoding="utf-8")
