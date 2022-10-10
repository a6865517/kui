from locust import HttpUser
from locust import TaskSet
from locust import task
from locust import events
import hashlib
import queue
from gevent._semaphore import Semaphore

all_locust_spawned = Semaphore()  # Semaphore: 信号量
all_locust_spawned.acquire()  # 信号量实例上锁

def on_hatch_complete(**kwargs):
    all_locust_spawned.release()  # 创建钩子函数

# 挂载钩子函数    为了让所有的locust示例产生完成后触发，进行钩子函数的监听状态
events.spawning_complete.add_listener(on_hatch_complete)

class UserTask(TaskSet):
    """用户任务类，用户的行为"""

    def on_start(self):
        payload = {
            "times": 1
        }
        res = self.client.post(url="/miaosha/reset3", data=payload)
        if res.json()["msg"] == "成功":
            print("商品重置成功")
        else:
            print("商品重置失败")

    def md5_pwd(self, pwd):
        md5 = hashlib.md5()
        md5.update(b"zr" + pwd.encode("utf8") + b"hg")
        return md5.hexdigest()

    @task
    def test_login(self):
        try:
            data = self.user.user_data_queue.get()  # get从队列里取值数据
        except queue.Empty:
            print("用户数据取完了")
            exit(0)  # 当队列里面的数据取完了，队列取完数据就停止运行，账号取值完后就停止运行   exit进行退出，正常退出

        payload = {
            "mobile": data,
            "password": self.md5_pwd("111111")
        }
        print(payload)
        with self.client.post(url="/login/login", data=payload, name="登录", catch_response=True) as res:
            if res.status_code == 200 and res.json()["msg"] == "成功":
                self.token = res.json()['data']
                res.success()  # 断言成功
            else:
                res.failure("登录失败")

    @task
    def test_get_goods_list(self):
        """获取商品列表请求"""
        with self.client.get(url="/goods/Jlist", name="获取商品列表", catch_response=True) as res:
            if res.status_code == 200 and res.json()["msg"] == "成功":
                res.success()
            else:
                res.failure("获取商品列表失败")

    @task
    def test_goods_detail(self):
        """获取商品详情"""
        with self.client.get(url=f"/goods/detail/1", name="获取商品详情", catch_response=True) as res:
            if res.status_code == 200 and res.json()["msg"] == "成功":
                res.success()
            else:
                res.failure("获取商品详情失败")

    @task
    def test_miaosha(self):
        """秒杀接口"""
        payload = {
            "goodsId": 1,
            "token": self.token
        }
        all_locust_spawned.wait()       # 限制在所有用户准备完成处于等待状态，实现集合点，类似jmeter同步定时器
        # 在这里wait等待，等待所有的用例加载完成以后然后去释放请求秒杀接口
        with self.client.post(url="/miaosha/miaosha", data=payload, name="秒杀接口", catch_response=True) as res:
            if res.status_code == 200 and res.json()["msg"] == "成功":
                res.success()
            else:
                res.failure("秒杀商品失败")

class WebSitUser(HttpUser):
    """定义用户类，访问用户"""
    tasks = [UserTask]
    host =
    min_wait = 2000
    max_wait = 3000
    user_data_queue = queue.Queue()
    for one in range(13588000000, 13588000999):
        user_data_queue.put(str(one))

if __name__ == '__main__':
    import os

    os.system("locust -f miaosha.py")