# -*- encoding: utf-8 -*-
"""
@File    : sqls.py
@Time    : 2022/6/17 16:45
@Author  : kui
@Software: PyCharm
"""
get_clinic_info_sql = 'SELECT term_clinic_id from term_clinic WHERE phone = %s'

get_gold_unbind_device_sno = 'SELECT sno from test_device WHERE device_type = 1 and status = 5 and term_clinic_id is NULL LIMIT 1'

get_blood_unbind_device_sno = 'SELECT sno from test_device WHERE device_type = 2 and status = 5 and term_clinic_id is NULL LIMIT 1'

get_device_id = 'SELECT test_device_id from test_device WHERE sno = %s'

get_clinic_bind_device_sno_gold = 'SELECT sno from test_device WHERE device_type = 1 and term_clinic_id = %s'

get_clinic_bind_device_sno_blood = 'SELECT sno from test_device WHERE device_type = 2 and term_clinic_id = %s'

revise_price_scheme = 'UPDATE term_clinic set test_strip_price_profit_scheme_id = 1004 WHERE term_clinic_id = %s'

check_user_exist = 'SELECT * from term_clinic WHERE phone = %s'