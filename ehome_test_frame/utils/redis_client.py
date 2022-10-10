# -*- encoding: utf-8 -*-
"""
@File    : redis_client.py
@Time    : 2022/7/16 17:37
@Author  : kui
@Software: PyCharm
"""
import redis
from utils import read_yaml,env


def redis_client():
    """
    创建redis连接池
    :return: rds:连接实例
    """
    connect_config = None
    ENV = env.env()
    try:
        connect_config = read_yaml.read(f'../config/{ENV}/{ENV}.yaml').get("redis")
    except AttributeError as e:
        print('config文件redis配置项有误', e)
    pool = redis.ConnectionPool(host=connect_config['host'], port=connect_config['port'],
                                password=connect_config['pwd'], db=connect_config['db'],
                                decode_responses=True)
    rds = redis.Redis(connection_pool=pool)
    return rds
