# -*- encoding: utf-8 -*-
"""
@File    : check_user_exist.py
@Time    : 2022/7/13 9:23
@Author  : kui
@Software: PyCharm
"""
from common import sqls
from utils import mysql_utils_test
from utils import mysql_utils_sta


def check_user_exist_test(phone):
    sql = sqls.check_user_exist
    data = mysql_utils_test.cursor_sql(sql, phone)
    if data:
        return True
    else:
        return False

def check_user_exist_sta(phone):
    sql = sqls.check_user_exist
    data = mysql_utils_sta.cursor_sql(sql, phone)
    if data:
        return True
    else:
        return False

if __name__ == '__main__':
    print(check_user_exist_test(1362222369))