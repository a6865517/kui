# -*- encoding: utf-8 -*-
"""
@File    : get_clinic_info.py
@Time    : 2022/6/17 16:16
@Author  : kui
@Software: PyCharm
"""
import requests
from utils import mysql_utils_sta,Log
from common import sqls, sta_data, sta_urls

log = Log.Log.log

def get_clinic_id(phone):
    """
    根据手机号码获取诊所ID
    :param phone:诊所手机号
    :return:诊所ID
    """
    sql = sqls.get_clinic_info_sql
    data = mysql_utils_sta.cursor_sql(sql, phone)
    clinicId = data[0]['term_clinic_id']
    return clinicId


def get_gold_device_sno():
    """
    获取未绑定的金标仪设备
    :return:设备sno
    """
    sql = sqls.get_gold_unbind_device_sno
    data = mysql_utils_sta.cursor_sql(sql)
    return data[0]['sno']


def get_blood_device_sno():
    """
    获取未绑定的血常规设备
    :return:设备sno
    """
    sql = sqls.get_blood_unbind_device_sno
    data = mysql_utils_sta.cursor_sql(sql)
    return data[0]['sno']


def get_gold_device_id(sno):
    """
    根据设备编号获取设备ID
    :param sno: 设备编号
    :return:设备sno
    """
    sql = sqls.get_device_id
    data = mysql_utils_sta.cursor_sql(sql, sno)
    return data[0]['test_device_id']


def bind_gold_blood_device(clinic_id, device_id, login_headers) -> None:
    """
    绑定设备
    :param login_headers:
    :param clinic_id: 诊所ID
    :param device_id: 设备id
    :return:
    """
    bind_device_data = sta_data.bind_device_data
    bind_device_url = sta_urls.bind_device_url
    bind_device_data['clinicId'] = clinic_id
    bind_device_data['ids'] = [device_id]
    r = requests.put(url=bind_device_url, json=bind_device_data, headers=login_headers)
    log.info('绑定设备接口请求参数' + str(bind_device_data))
    log.info('绑定设备接口返回参数' + str(r.text))


def get_clinic_bind_device_sno_gold(clinic_id):
    """
    获取当前诊所绑定的金标仪设备编号
    :param clinic_id: 诊所ID
    :return: 设备编号
    """
    sql = sqls.get_clinic_bind_device_sno_gold
    sno = mysql_utils_sta.cursor_sql(sql, clinic_id)
    return sno[0]['sno']


def get_clinic_bind_device_sno_blood(clinic_id):
    """
    获取当前诊所绑定的血常规设备编号
    :param clinic_id: 诊所ID
    :return: 设备编号
    """
    sql = sqls.get_clinic_bind_device_sno_blood
    sno = mysql_utils_sta.cursor_sql(sql, clinic_id)
    return sno[0]['sno']


def test_main(phone,login_headers) -> None:
    """
    前置操作
    """
    clinic_id = get_clinic_id(phone)
    gold_device_sno = get_gold_device_sno()
    blood_device_sno = get_blood_device_sno()
    gold_device_id = get_gold_device_id(gold_device_sno)
    blood_device_id = get_gold_device_id(blood_device_sno)
    bind_gold_blood_device(clinic_id, gold_device_id, login_headers)
    bind_gold_blood_device(clinic_id, blood_device_id, login_headers)


if __name__ == '__main__':
    pass
