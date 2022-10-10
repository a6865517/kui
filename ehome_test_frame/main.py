import os
import time
import pytest


if __name__ == '__main__':
    pytest.main()
    times = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
    os.system(f"allure generate ./temp -o ./report/report_{times} --clean")