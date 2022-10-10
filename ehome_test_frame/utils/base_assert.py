# -*- encoding: utf-8 -*-
"""
@File    : base_assert.py
@Time    : 2022/7/19 16:45
@Author  : kui
@Software: PyCharm
"""
from utils import logger

log = logger.log


def base_assert(res, *args, **kwargs) -> None:
    """
    基础断言
    :param res:
    :param args:
    :param kwargs:
    :return:
    """
    busiCode = None
    msg = None
    res_time = res.elapsed.total_seconds()
    log.info('本次请求响应参数为:' + str(res.json()))
    assert res_time < 5, log.warning('接口响应时间超过5秒')
    for _ in args, kwargs:
        if _:
            busiCode = _[0]['asserts']['response']['busiCode']
            msg = _[0]['asserts']['response']['msg']
    assert res.json()['busiCode'] == busiCode, log.error(
        f'busiCode与预期值不符,期望返回busiCode为：{busiCode},实际返回busiCode为：{str(res.json()["busiCode"])}')
    assert res.json()['msg'] == msg, log.error(f'msg与预期值不符,期望返回msge为：{msg},实际返回msg为：{str(res.json()["msg"])}')
