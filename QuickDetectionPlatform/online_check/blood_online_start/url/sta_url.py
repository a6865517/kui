# -*- encoding: utf-8 -*-
"""
@File    : test_url.py
@Time    : 2022/6/17 18:35
@Author  : kui
@Software: PyCharm
"""
api = 'http://sta-client-api.ehomepoct.com/'

add_patient = api + 'palmpoct-client/api/patient/savePatient'

upload_patient = api + 'palmpoct-client/api/new/online/upload/patient'

crp_saa_check = api + 'palmpoct-client/testanalysis/dotestanalysis'

create_order = api + 'palmpoct-client/api/new/online/create/order'

blood_order_palce = 'https://check-staging.ehomepoct.com/blood-cell-analysis/order/palce'

blood_test = 'http://check-staging.ehomepoct.com/blood-cell-analysis/check/start'

call_back = api + 'palmpoct-client/api/order/qr/callBack'
