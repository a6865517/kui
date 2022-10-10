# -*- encoding: utf-8 -*-
"""
@File    : agentTestCase.py
@Time    : 2022/4/11 14:36
@Author  : kui
@Software: PyCharm
"""


from ddt import ddt, file_data
from common import unittestMain
from utils import my_utils


@ddt
class TestAgent(unittestMain.UnittestMain):
    """
    测试用例集
    """

    @file_data('../data/agent_query/queryEveryDayData.yaml')
    def test_001_post_queryEveryDayData(self, **kwargs):
        """
        按日期查询范围内每日合伙人数据
        """
        r = self.req_request(**kwargs)
        if r.status_code == 200:
            print(r.text)
            self.req_assert(r, **kwargs)
            self.assert_data(r, **kwargs)
        else:
            self.fail('接口请求失败,status_code非200')

    @file_data('../data/agent_query/queryRatioData.yaml')
    def test_002_post_queryRatioData(self, **kwargs):
        """
        按日期维度查询合伙人环比数据
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryClinicData.yaml')
    def test_003_post_queryClinicData(self, **kwargs):
        """
        查询诊所统计数据
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryClinicList.yaml')
    def test_004_post_queryClinicList(self, **kwargs):
        """
        查询诊所列表数据
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryClinicRingRatioData.yaml')
    def test_005_post_queryClinicRingRatioData(self, **kwargs):
        """
        查询诊所环比数据
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryBindDeviceListData.yaml')
    def test_006_post_queryBindDeviceListData(self, **kwargs):
        """
        查询当日绑定诊所列表
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryEveryDayDataDevice.yaml')
    def test_007_post_queryEveryDayDataDevice(self, **kwargs):
        """
        按日期查询范围内每日绑定诊所数据
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryRatioDataDevice.yaml')
    def test_008_post_queryRatioDataDevice(self, **kwargs):
        """
        按日期维度查询绑定诊所环比数据
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryIndexData.yaml')
    def test_009_get_queryIndexData(self, **kwargs):
        """
        查询首页统计数据
        """
        r = self.req_request(methods='get', **kwargs)
        if r.status_code == 200:
            print(r.text)
            self.req_assert(r, **kwargs)
            self.assert_data(r, **kwargs)
        else:
            self.fail('接口请求失败,status_code非200')

    @file_data('../data/agent_query/queryClinicTestData.yaml')
    def test_010_post_queryClinicTestData(self, **kwargs):
        """
        查询诊所检测统计数据
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryTestData.yaml')
    def test_011_post_queryTestData(self, **kwargs):
        """
        查询检测统计数据
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryTestProjectData.yaml')
    def test_012_post_queryTestProjectData(self, **kwargs):
        """
        查询检测项目统计数据
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryTestRingNewRatioData.yaml')
    def test_013_post_queryTestRingNewRatioData(self, **kwargs):
        """
        查询检测环比数据
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent/createAgent.yaml')
    def test_014_post_createAgent(self, **kwargs):
        """
        创建合伙人
        """
        kwargs['data']['verifyCode'] = my_utils.get_register_code()
        self.assert_all(**kwargs)

    @file_data('../data/agent/modifyAgent.yaml')
    def test_015_put_modifyAgent(self, **kwargs):
        """
        修改合伙人
        """
        r = self.req_request(methods='put', **kwargs)
        if r.status_code == 200:
            print(r.text)
            self.req_assert(r, **kwargs)
            self.assert_data(r, **kwargs)
        else:
            self.fail('接口请求失败,status_code非200')

    @file_data('../data/agent/verifyCodesSend.yaml')
    def test_016_post_verifyCodesSend(self, **kwargs):
        """
        发送验证码
        """
        self.assert_all(**kwargs)
        my_utils.del_test_code(kwargs['data']['phone'])

    @file_data('../data/agent_query/queryAgentLevelCount.yaml')
    def test_017_post_queryAgentLevelCount(self, **kwargs):
        """
        查询合伙人下级各级合伙人数量,包含终端门诊数
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryAgentListData.yaml')
    def test_018_post_queryAgentListData(self, **kwargs):
        """
        按日期查询合伙人列表分页
        """
        self.assert_all(**kwargs)

    @file_data('../data/agent_query/queryAgentListDataByPeriod.yaml')
    def test_019_post_queryAgentListDataByPeriod(self, **kwargs):
        """
        按日期段查询合伙人列表分页
        """
        self.assert_all(**kwargs)
