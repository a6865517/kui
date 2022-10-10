# -*- encoding: utf-8 -*-
"""
@File    : test_data.py
@Time    : 2022/6/18 10:00
@Author  : kui
@Software: PyCharm
"""
add_patient = {"age": 18,"deviceId": None,"month": 0,"name": "华强测试","phone": "13622220000","sex": 0,"termClinicId": None}

crp_saa_check = {"clinicId": None,"sno": None}

create_order = {"addressDetail": "湖南省长沙市雨花区华坤时代","briefAddress": "湖南省长沙市雨花区雨河路279号靠近湘府路站","latitude": 113.029384,"longitude": 28.111673,"recordId": None,"sno": None,"testDataIds": [None]}


blood_test = {"boardSno": "220301360723","cameraName": "测试相机","clinicId": None,"deviceSno": None,"hgbCalibration": [
        {
                    "reference": 20317,
                    "groundTruth": 0,
                    "measure": 25501
                },
                {
                    "reference": 20732,
                    "groundTruth": 0,
                    "measure": 25637
                },
                {
                    "reference": 19684,
                    "groundTruth": 231,
                    "measure": 2397
                },
                {
                    "reference": 20401,
                    "groundTruth": 141,
                    "measure": 6061
                },
                {
                    "reference": 20628,
                    "groundTruth": 71,
                    "measure": 12633
                },
                {
                    "reference": 20360,
                    "groundTruth": 48,
                    "measure": 15893
                }
            ],"hgbCurveData": [],"hgbMeasure": 0,"hgbReference": 0,"path": "c69099f6-2df3-497b-b5ac-cefdca802aa9.zip","patientId": None,"pointConfig": {
                "plt": {
                    "focus": 0,
                    "points": 0
                },
                "rbc": {
                    "focus": 0,
                    "points": 0
                },
                "wbc": {
                    "focus": 0,
                    "points": 0
                }
            },"type": 2}


blood_order_palce= {"dataId": None,"recordId": None}

call_back = {"openId": "111111111111","orderNo": '',"outOrderNo": "111111111111111","outTransactionNo": "111111111111111111111","payChannel": "0","payFinishTime": "2021-10-02 18:27:00","payStatus": "SUCCESS","payType": "WXPAY","tradeType": "JSAPI"}