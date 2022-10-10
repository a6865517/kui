# -*- encoding: utf-8 -*-
"""
@File    : blood_check_test.py
@Time    : 2022/6/18 9:39
@Author  : kui
@Software: PyCharm
"""
import datetime
import time

import requests
from common import sqls
from utils import get_clinic_info_sta, login, Log, mysql_utils_sta
from online_check.blood_online_start.data import sta_data
from online_check.blood_online_start.url import sta_url


log = Log.Log.log


class bloodCheckSta:
    """预发布环境血常规联测"""

    def __init__(self, phone):
        self.phone = phone
        self.login_headers = login.login_sta()
        self.bind_device()
        self.clinic_id = get_clinic_info_sta.get_clinic_id(self.phone)
        self.gold_sno = get_clinic_info_sta.get_clinic_bind_device_sno_gold(self.clinic_id)
        self.blood_sno = get_clinic_info_sta.get_clinic_bind_device_sno_blood(self.clinic_id)
        self.patientId = self.add_patient()
        self.testPoctDataId = self.start_CRP_and_SAA()
        self.recordId = self.upload_patient()
        self.blood_test_id = self.blood_test()
        self.orderNo = self.order_palce_blood()

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

    def upload_patient(self):
        """
        发布患者信息
        :return:dataID
        """
        sta_data.add_patient['termClinicId'] = self.clinic_id
        sta_data.add_patient['deviceId'] = self.gold_sno
        res = requests.post(url=sta_url.upload_patient, json=sta_data.add_patient, headers=self.login_headers)
        log.info('发布患者信息接口请求参数为:' + str(sta_data.add_patient))
        log.info('发布患者信息接口响应参数为:' + str(res.text))
        return res.json()['data']


    def start_CRP_and_SAA(self):
        """
        进行其他两项检测
        :return: testPoctDataId
        """
        sta_data.crp_saa_check['clinicId'] = self.clinic_id
        sta_data.crp_saa_check['sno'] = self.gold_sno
        file_crp = {"file": open(f"./online_check/blood_online_start/data/CRP.jpg", "rb")}
        file_saa = {"file": open(f"./online_check/blood_online_start/data/SAA.jpg", "rb")}
        r_crp = requests.post(sta_url.crp_saa_check, headers=self.login_headers, data=sta_data.crp_saa_check, files=file_crp)
        r_saa = requests.post(sta_url.crp_saa_check, headers=self.login_headers, data=sta_data.crp_saa_check, files=file_saa)
        log.info('crp+saa检测接口请求参数为:' + str(sta_data.crp_saa_check))
        log.info('crp+saa检测接口响应参数为:' + str(r_crp.text))
        return [r_crp.json()['data']['testPoctDataId'], r_saa.json()['data']['testPoctDataId']]


    def create_order(self):
        """
        金标仪创建联测订单
        :return:
        """
        sta_data.create_order['recordId'] = self.recordId
        sta_data.create_order['sno'] = self.gold_sno
        sta_data.create_order['testDataIds'] = self.testPoctDataId
        r = requests.post(sta_url.create_order,json=sta_data.create_order,headers=self.login_headers)
        log.info('金标仪创建联测订单接口请求参数为:' + str(sta_data.create_order))
        log.info('金标仪创建联测订单接口响应参数为:' + str(r.text))


    def blood_test(self):
        """
        血常规检测
        :return:dataId
        """
        sta_data.blood_test['clinicId'] = self.clinic_id
        sta_data.blood_test['deviceSno'] = self.blood_sno
        sta_data.blood_test['patientId'] = self.patientId
        r = requests.post(sta_url.blood_test,headers=self.login_headers,json=sta_data.blood_test)
        log.info('血常规检测接口请求参数为:' + str(sta_data.blood_test))
        log.info('血常规检测接口响应参数为:' + str(r.text))
        return r.json()['data']


    def get_manual_status(self) -> None:
        """
        等待算法完成查询状态
        :return:
        """
        url = f'https://check-staging.ehomepoct.com/blood-cell-analysis/check/manual/status/{self.blood_test_id}'
        r = requests.get(url, headers=self.login_headers)
        time.sleep(1)
        log.info('等待一秒钟，再去查询')
        log.info('查询算法接口结果' + str(r.json()))
        if r.json()['data']['status'] == 1:
            self.get_manual_status()

    def order_palce_blood(self):
        """
        血常规下单
        :return:orderNo 订单编号
        """
        self.get_manual_status()
        sta_data.blood_order_palce['dataId'] = self.blood_test_id
        sta_data.blood_order_palce['recordId'] = self.recordId
        r = requests.post(sta_url.blood_order_palce, headers=self.login_headers, json=sta_data.blood_order_palce)
        log.info('血常规下单接口请求参数为:' + str(sta_data.blood_order_palce))
        log.info('血常规下单接口响应参数为:' + str(r.text))
        if r.json()['busiCode'] == 0:
            return r.json()['data']['orderNo']

    def call_back(self):
        """
        支付回调
        :return:status,状态
        """
        status = False
        now_time = datetime.datetime.now()
        offset = datetime.timedelta(minutes=1)
        re_date = (now_time + offset).strftime('%Y-%m-%d %H:%M:%S')
        sta_data.call_back['payFinishTime'] = re_date
        sta_data.call_back['orderNo'] = self.orderNo
        r = requests.post(url=sta_url.call_back, json=sta_data.call_back, headers=self.login_headers)
        log.info('支付回调接口请求参数为：' + str(sta_data.call_back))
        log.info('支付回调接口响应内容为:' + str(r.text))
        if self.orderNo is not None:
            status = True
        return status



if __name__ == '__main__':
    Blood_check = bloodCheckSta(13622223661)
    Blood_check.call_back()
