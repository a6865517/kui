# -*- encoding: utf-8 -*-
"""
@File    : main_gold.py
@Time    : 2022/6/29 11:09
@Author  : kui
@Software: PyCharm
"""
from utils import Log
import requests

log = Log.Log.log

def login():
    """
    正式环境-登录
    :return: token
    """
    url = 'http://client-c.ehomepoct.com/palmpoct-client/api/login/byPwd'
    data =   {'account': '13622223661', 'code': '', 'password': 'a6865517'}
    r = requests.post(url=url, json=data)
    token = r.json()['data']['token']
    log.info('本次登录获取token为:' + str({'Authorization': token}))
    return {'Authorization': token}



CRP_SAA = {'file': open('../enum_mold/data/CRP+SAA.jpg', 'rb')}
create_order =  {"addressDetail": "湖南省长沙市雨花区华坤时代","briefAddress": "湖南省长沙市雨花区雨河路279号靠近湘府路站","clinicId": None,"latitude": 0,"longitude": 0,"patientId": None,"position": "湖南省长沙市雨花区华坤时代","sno": None,"testDataIds": []}

api = 'http://client-c.ehomepoct.com/'

add_patient_url = api + 'palmpoct-client/api/patient/savePatient'

start_check_url = api + 'palmpoct-client/testanalysis/newdotestanalysis'

create_order_url = api + 'palmpoct-client/testanalysis/docreatereportorder'


add_patient = {"age": 18,"deviceId": None,"month": 0,"name": "华强测试","phone": "13622220000","sex": 0,"termClinicId": None}
check_data = {'clinicId': None, "file": None, 'sno': None}

class GoldCheckTest:
    """正式环境环境金标仪单测"""

    def __init__(self,clinic_id,gold_sno):
        self.login_headers = login()
        self.clinic_id = clinic_id
        self.gold_sno = gold_sno
        self.patientId = self.add_patient()
        self.testPoctDataId = self.start_check()


    def add_patient(self):
        """
        添加患者
        :return:患者ID
        """
        add_patient['termClinicId'] = self.clinic_id
        add_patient['deviceId'] = self.gold_sno
        res = requests.post(url=add_patient_url, json=add_patient, headers=self.login_headers)
        log.info('添加患者接口请求参数为:' + str(add_patient))
        log.info('添加患者接口响应参数为:' + str(res.text))
        return res.json()['data']['patientId']

    def start_check(self):
        """
        开始检测
        :return:status 成功状态
        """
        check_data['clinicId'] = self.clinic_id
        check_data['sno'] = self.gold_sno
        res = requests.post(url=start_check_url, data=check_data, files=CRP_SAA,
                            headers=self.login_headers)
        log.info('开始检测接口请求参数为：' + str(check_data))
        log.info('开始检测接口响应内容为:' + str(res.text))
        if res.json()['busiCode'] == 0:
            return res.json()['data']['testPoctDataId']
        else:
            log.error('开始检测接口响应结果错误，busiCode非预期值：0')

    def create_order_main(self):
        """
        生成订单
        :return:orderNo，订单编号
        """
        orderNo = None
        create_order['testDataIds'] = self.testPoctDataId
        create_order['clinicId'] = self.clinic_id
        create_order['patientId'] = self.patientId
        create_order['sno'] = self.gold_sno
        r = requests.post(create_order_url, json=create_order, headers=self.login_headers)
        log.info('生成订单接口请求参数为：' + str(create_order))
        log.info('生成订单接口响应内容为:' + str(r.text))
        if r.json()['busiCode'] == 0:
            orderNo = r.json()['data']['orderNo']
        return orderNo


if __name__ == '__main__':
    Blood_check = GoldCheckTest(1542339550324760577, 'B12345678900001')
    Blood_check.create_order_main()
