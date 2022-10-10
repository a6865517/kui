# -*- encoding: utf-8 -*-
"""
@File    : test_url.py
@Time    : 2022/6/17 18:35
@Author  : kui
@Software: PyCharm
"""
api = 'http://check-gateway.ehomepoct.com/'

add_patient = api + 'blood-cell-analysis/patient/patient/add' # 添加患者

start_check = api + 'blood-cell-analysis/check/start' # 开始检测

create_order = api + 'blood-cell-analysis/order/palce' # 创建订单

call_back = 'http://test-client.ehomepoct.com/palmpoct-client/api/order/qr/callBack' # 支付回调
