# -*- encoding: utf-8 -*-
"""
@File    : blood_check_test.py
@Time    : 2022/6/18 9:39
@Author  : kui
@Software: PyCharm
"""
from blood_check import blood_check_test, blood_check_sta
from gold_check import gold_check_test, gold_check_sta
from online_check.blood_online_start import blood_online_test, blood_online_sta
from online_check.gold_online_start import gold_online_test, gold_online_sta
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from utils import Log,check_user_exist

log = Log.Log.log
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/index', methods=['GET'])
def index():
    """首页"""
    return render_template("index.html")


@app.route('/test/gold_check', methods=['POST'])
def _gold_check_test():
    """金标仪测试环境"""
    res_data = {'code': 0, 'msg': '检测完成', 'data': []}
    res = res_data
    test_type = request.form['paperCode']
    phone = request.form['phone']
    if check_user_exist.check_user_exist_test(phone) is False:
        res['code'] = -2
        res['msg'] = '该用户未注册诊所账户,你在搞什么飞机'
        log.success('本次请求响应内容为' + str(res))
        return jsonify(res)
    gold_check_test_case = gold_check_test.GoldCheckTest(phone, test_type)
    status = gold_check_test_case.call_back()
    if status is not True:
        res['code'] = -1
        res['msg'] = '检测接口异常'
    log.success('本次请求响应内容为' + str(res))
    return jsonify(res)


@app.route('/sta/gold_check', methods=['POST'])
def _gold_check_sta():
    """金标仪预发布环境"""
    res_data = {'code': 0, 'msg': '检测完成', 'data': []}
    res = res_data
    test_type = request.form['paperCode']
    phone = request.form['phone']
    if check_user_exist.check_user_exist_sta(phone) is False:
        res['code'] = -2
        res['msg'] = '该用户未注册诊所账户,你在搞什么飞机'
        log.success('本次请求响应内容为' + str(res))
        return jsonify(res)
    gold_check_sta_case = gold_check_sta.GoldCheckSta(phone, test_type)
    status = gold_check_sta_case.call_back()
    if status is not True:
        res['code'] = -1
        res['msg'] = '检测接口异常'
    log.success('本次请求响应内容为' + str(res))
    return jsonify(res)


@app.route('/test/blood_check', methods=['POST'])
def _blood_check_test():
    """血常规测试环境"""
    res_data = {'code': 0, 'msg': '检测完成', 'data': []}
    res = res_data
    phone = request.form['phone']
    if check_user_exist.check_user_exist_test(phone) is False:
        res['code'] = -2
        res['msg'] = '该用户未注册诊所账户,你在搞什么飞机'
        log.success('本次请求响应内容为' + str(res))
        return jsonify(res)
    blood_check_test_case = blood_check_test.BloodCheckTest(phone)
    status = blood_check_test_case.call_back()
    if status is not True:
        res['code'] = -1
        res['msg'] = '检测接口异常'
    log.success('本次请求响应内容为' + str(res))
    return jsonify(res)


@app.route('/sta/blood_check', methods=['POST'])
def _blood_check_sta():
    """血常规预发布环境"""
    res_data = {'code': 0, 'msg': '检测完成', 'data': []}
    res = res_data
    phone = request.form['phone']
    if check_user_exist.check_user_exist_sta(phone) is False:
        res['code'] = -2
        res['msg'] = '该用户未注册诊所账户,你在搞什么飞机'
        log.success('本次请求响应内容为' + str(res))
        return jsonify(res)
    blood_check_sta_case = blood_check_sta.BloodCheckSta(phone)
    status = blood_check_sta_case.call_back()
    if status is not True:
        res['code'] = -1
        res['msg'] = '检测接口异常'
    log.success('本次请求响应内容为' + str(res))
    return jsonify(res)


@app.route('/test/online_gold_check', methods=['POST'])
def _online_gold_check_test():
    """金标仪发起联测测试环境"""
    res_data = {'code': 0, 'msg': '检测完成', 'data': []}
    res = res_data
    phone = request.form['phone']
    if check_user_exist.check_user_exist_test(phone) is False:
        res['code'] = -2
        res['msg'] = '该用户未注册诊所账户,你在搞什么飞机'
        log.success('本次请求响应内容为' + str(res))
        return jsonify(res)
    online_gold_check_test_case = gold_online_test.GoldCheckTest(phone)
    status = online_gold_check_test_case.call_back()
    if status is not True:
        res['code'] = -1
        res['msg'] = '检测接口异常'
    log.success('本次请求响应内容为' + str(res))
    return jsonify(res)


@app.route('/sta/online_gold_check', methods=['POST'])
def _online_gold_check_sta():
    """金标仪发起联测预发布环境"""
    res_data = {'code': 0, 'msg': '检测完成', 'data': []}
    res = res_data
    phone = request.form['phone']
    if check_user_exist.check_user_exist_sta(phone) is False:
        res['code'] = -2
        res['msg'] = '该用户未注册诊所账户,你在搞什么飞机'
        log.success('本次请求响应内容为' + str(res))
        return jsonify(res)
    online_gold_check_sta_case = gold_online_sta.GoldCheckSta(phone)
    status = online_gold_check_sta_case.call_back()
    if status is not True:
        res['code'] = -1
        res['msg'] = '检测接口异常'
    log.success('本次请求响应内容为' + str(res))
    return jsonify(res)


@app.route('/test/online_blood_check', methods=['POST'])
def _online_blood_check_test():
    """血常规发起联测测试环境"""
    res_data = {'code': 0, 'msg': '检测完成', 'data': []}
    res = res_data
    phone = request.form['phone']
    if check_user_exist.check_user_exist_test(phone) is False:
        res['code'] = -2
        res['msg'] = '该用户未注册诊所账户,你在搞什么飞机'
        log.success('本次请求响应内容为' + str(res))
        return jsonify(res)
    online_blood_check_test_case = blood_online_test.bloodCheckTest(phone)
    status = online_blood_check_test_case.call_back()
    if status is not True:
        res['code'] = -1
        res['msg'] = '检测接口异常'
    log.success('本次请求响应内容为' + str(res))
    return jsonify(res)


@app.route('/sta/online_blood_check', methods=['POST'])
def _online_blood_check_sta():
    """血常规发起联测预发布环境"""
    res_data = {'code': 0, 'msg': '检测完成', 'data': []}
    res = res_data
    phone = request.form['phone']
    if check_user_exist.check_user_exist_sta(phone) is False:
        res['code'] = -2
        res['msg'] = '该用户未注册诊所账户,你在搞什么飞机'
        log.success('本次请求响应内容为' + str(res))
        return jsonify(res)
    online_blood_check_sta_case = blood_online_sta.bloodCheckSta(phone)
    status = online_blood_check_sta_case.call_back()
    if status is not True:
        res['code'] = -1
        res['msg'] = '检测接口异常'
    log.success('本次请求响应内容为' + str(res))
    return jsonify(res)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)
