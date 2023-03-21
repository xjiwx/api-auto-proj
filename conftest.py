import pytest
import requests
from testFunctions.logger import Log
@pytest.fixture()
def login():
    s = requests.Session()
    res = s.post(url='http://novel.hctestedu.com/user/login', data={"username": "17701293276", "password": "123456"})
    cookiejar = res.cookies.get_dict()
    x = res.json()
    cookiejar['Authorization'] = x['data']['token']
    # 把字典变成一个键值对用'='相连，不同键值对用';'隔开 的字符串
    cookie_string = ';'.join(str(x) + '=' + str(y) for x, y in cookiejar.items())
    headers = {
        'Cookie': cookie_string
    }

    return headers

# @pytest.fixture(autouse=True)
# def func1():
#     log = Log()
#     log.info('开始测试')
#     yield
#     log.info('结束测试')

