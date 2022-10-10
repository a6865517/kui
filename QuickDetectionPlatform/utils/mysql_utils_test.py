# -*- coding:utf-8 -*-
"""
@Author: kui
@File:  MysqlUtils.py
@CreateTime:  2021-09-30
@desc: TODO 创建pymysql类
"""
from common import config
from dbutils.pooled_db import PooledDB
import pymysql

db_host = config.test_mysql_info


class CreateEngine:
    pool = None

    def __init__(self, mincached=10, maxcached=20, maxshared=10, maxconnections=200, blocking=True,
                 maxusage=100, setsession=None, reset=True, host=db_host['host'], user=db_host['root'],
                 password=db_host['password'],
                 port=db_host['port'],
                 charset=db_host['charset'], database=db_host['database']):
        """
        :param mincached:连接池中空闲连接的初始数量
        :param maxcached:连接池中空闲连接的最大数量
        :param maxshared:共享连接的最大数量
        :param maxconnections:创建连接池的最大数量
        :param blocking:超过最大连接数量时候的表现，为True等待连接数量下降，为false直接报错处理
        :param maxusage:单个连接的最大重复使用次数
        """
        if not self.pool:
            self.pool = PooledDB(pymysql,
                                 mincached, maxcached,
                                 maxshared, maxconnections, blocking,
                                 maxusage, setsession, reset,
                                 host=host, port=port, db=database,
                                 user=user, passwd=password,
                                 charset=charset,
                                 cursorclass=pymysql.cursors.DictCursor
                                 )

    def get_conn(self):
        """
        连接池返回一个连接
        :return: conn 连接属性
        """
        conn = self.pool.connection()
        return conn


createEngine = CreateEngine()


def cursor_sql(sql, *args):
    """
    执行sql cursor_sql(),查询语句
    """
    try:
        conn = createEngine.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        data = cursor.fetchall()
    except Exception as e:
        print('=' * 20 + '未连接数据库或sql语法错误' + '=' * 20)
        raise e
    finally:
        if conn:
            conn.close()
    return data


def update_sql(sql, list):
    """
        执行sql insert_sql()，插入语句
        """
    try:
        cur = createEngine.get_conn()
        cursor = cur.cursor()
        cursor.execute(sql, list)
        cur.commit()
        print('-' * 100 + '更新成功' + '-' * 100)
    except Exception as e:
        print('=' * 20 + '未连接数据库或sql语法错误' + '=' * 20)
        raise e
    finally:
        cur.close()
