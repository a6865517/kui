# -*- encoding: utf-8 -*-
"""
@File    : blood_check_test.py
@Time    : 2022/6/18 9:39
@Author  : kui
@Software: PyCharm
"""
import datetime
import requests
from common import sqls
from utils import get_clinic_info_sta, login, Log, mysql_utils_sta, enum_mold
from gold_check.data import sta_data
from gold_check.url import sta_url

log = Log.Log.log

class GoldCheckSta:
    """预发布环境金标仪单测"""

    def __init__(self, phone,num):
        self.phone = phone
        self.login_headers = login.login_sta()
        self.bind_device()
        self.test_name = enum_mold.get_mold(num)
        self.clinic_id = get_clinic_info_sta.get_clinic_id(self.phone)
        self.gold_sno = get_clinic_info_sta.get_clinic_bind_device_sno_gold(self.clinic_id)
        self.patientId = self.add_patient()
        self.testPoctDataId = self.start_check()
        self.orderNo = self.create_order()

    def bind_device(self) -> None:
        """
        进行绑定设备的前置操作
        :return:
        """
        get_clinic_info_sta.test_main(self.phone, self.login_headers)

    def revise_price_scheme(self) -> None:
        """
        修改价格方案
        :return:
        """
        sql = sqls.revise_price_scheme
        mysql_utils_sta.update_sql(sql, self.clinic_id)

    def add_patient(self):
        """
        添加患者
        :return:患者ID
        """
        self.revise_price_scheme()
        sta_data.add_patient['termClinicId'] = self.clinic_id
        sta_data.add_patient['deviceId'] = self.gold_sno
        res = requests.post(url=sta_url.add_patient, json=sta_data.add_patient, headers=self.login_headers)
        log.info('添加患者接口请求参数为:' + str(sta_data.add_patient))
        log.info('添加患者接口响应参数为:' + str(res.text))
        return res.json()['data']['patientId']

    def start_check(self):
        """
        开始检测
        :return:status 成功状态
        """
        sta_data.check_data['clinicId'] = self.clinic_id
        sta_data.check_data['sno'] = self.gold_sno
        res = requests.post(url=sta_url.start_check, data=sta_data.check_data,files=self.test_name,headers=self.login_headers)
        log.info('开始检测接口请求参数为：' + str(sta_data.check_data))
        log.info('开始检测接口响应内容为:' + str(res.text))
        if res.json()['busiCode'] == 0:
            return res.json()['data']['testPoctDataId']
        else:
            log.error('开始检测接口响应结果错误，busiCode非预期值：0')



    def create_order(self):
        """
        生成订单
        :return:orderNo，订单编号
        """
        orderNo = None
        sta_data.create_order['testDataIds'] = self.testPoctDataId
        sta_data.create_order['clinicId'] = self.clinic_id
        sta_data.create_order['sno'] = self.gold_sno
        sta_data.create_order['patientId'] = self.patientId
        r = requests.post(sta_url.create_order,json=sta_data.create_order,headers=self.login_headers)
        log.info('生成订单接口请求参数为：' + str(sta_data.create_order))
        log.info('生成订单接口响应内容为:' + str(r.text))
        if r.json()['busiCode'] == 0:
            orderNo = r.json()['data']['orderNo']
        return orderNo


    def call_back(self):
        """
        支付回调
        :return:status,状态
        """
        status = False
        now_time = datetime.datetime.now()
        offset = datetime.timedelta(minutes=3)
        re_date = (now_time + offset).strftime('%Y-%m-%d %H:%M:%S')
        sta_data.call_back['payFinishTime'] = re_date
        sta_data.call_back['orderNo'] = self.orderNo
        r = requests.post(url=sta_url.call_back, json=sta_data.call_back, headers=self.login_headers)
        log.info('支付回调接口请求参数为：' + str(sta_data.check_data))
        log.info('支付回调接口响应内容为:' + str(r.text))
        if self.orderNo is not None:
            status = True
        return status


if __name__ == '__main__':
    Blood_check = GoldCheckSta(13622223661,0)
    Blood_check.call_back()
