# -*- encoding: utf-8 -*-
"""
@File    : test_mold.py
@Time    : 2022/6/21 10:29
@Author  : kui
@Software: PyCharm
"""
def get_mold(num):
    """
    试纸地址,多路径获取
    """
    test_name = None
    try:
        CRP = {'file': open('../check_data/CRP.jpg', 'rb')}
        SAA = {'file': open('../check_data/SAA.jpg', 'rb')}
        MP_lgM = {'file': open('../check_data/MP-lgM.jpg', 'rb')}
        Cpn_lgM = {'file': open('../check_data/Cpn-lgM.jpg', 'rb')}
        MP_Ab = {'file': open('../check_data/MP-Ab.jpg', 'rb')}
        EV71 = {'file': open('../check_data/EV71.jpg', 'rb')}
        CVA16 = {'file': open('../check_data/CVA16.jpg', 'rb')}
        FluAB_Ag = {'file': open('../check_data/FluA+B.jpg', 'rb')}
        HP_lgM_lgG = {'file': open('../check_data/HP-lgM-lgG.jpg', 'rb')}
        mALb = {'file': open('../check_data/mALb.jpg', 'rb')}
        HbA1C = {'file': open('../check_data/HbA1C.jpg', 'rb')}
        CRP_SAA = {'file': open('../check_data/CRP+SAA.jpg', 'rb')}
    except IOError:
        CRP = {'file': open('./check_data/CRP.jpg', 'rb')}
        SAA = {'file': open('./check_data/SAA.jpg', 'rb')}
        MP_lgM = {'file': open('./check_data/MP-lgM.jpg', 'rb')}
        Cpn_lgM = {'file': open('./check_data/Cpn-lgM.jpg', 'rb')}
        MP_Ab = {'file': open('./check_data/MP-Ab.jpg', 'rb')}
        EV71 = {'file': open('./check_data/EV71.jpg', 'rb')}
        CVA16 = {'file': open('./check_data/CVA16.jpg', 'rb')}
        FluAB_Ag = {'file': open('./check_data/FluA+B.jpg', 'rb')}
        HP_lgM_lgG = {'file': open('./check_data/HP-lgM-lgG.jpg', 'rb')}
        mALb = {'file': open('./check_data/mALb.jpg', 'rb')}
        HbA1C = {'file': open('./check_data/HbA1C.jpg', 'rb')}
        CRP_SAA = {'file': open('./check_data/CRP+SAA.jpg', 'rb')}
    if int(num) == 0:
        test_name = CRP
    elif int(num) == 1:
        test_name = SAA
    elif int(num) == 2:
        test_name = MP_lgM
    elif int(num) == 3:
        test_name = Cpn_lgM
    elif int(num) == 4:
        test_name = MP_Ab
    elif int(num) == 5:
        test_name = EV71
    elif int(num) == 6:
        test_name = CVA16
    elif int(num) == 7:
        test_name = FluAB_Ag
    elif int(num) == 8:
        test_name = HP_lgM_lgG
    elif int(num) == 9:
        test_name = mALb
    elif int(num) == 10:
        test_name = HbA1C
    elif int(num) == 11:
        test_name = CRP_SAA
    else:
        print('试纸未定义')
    return test_name


if __name__ == '__main__':
    pass
