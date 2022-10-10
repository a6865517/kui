# -*- encoding: utf-8 -*-
"""
@File    : sta_url.py
@Time    : 2022/6/17 18:35
@Author  : kui
@Software: PyCharm
"""
api = 'https://check-staging.ehomepoct.com/'

add_patient = api + 'blood-cell-analysis/patient/patient/add'

start_check = api + 'blood-cell-analysis/check/start'

create_order = api + 'blood-cell-analysis/order/palce'

call_back = 'http://sta-client-api.ehomepoct.com/palmpoct-client/api/order/qr/callBack'
