import pytest
from testFunctions.get_testdata import get_td
from testFunctions.request import Request
from testFunctions.logger import Log

@pytest.mark.parametrize('tu',get_td())
def test_main(login,tu):
    log = Log()
    log.info('当前是第{}条测试用例：{}'.format(int(tu['id']),tu['description']))
    log.info('测试数据是{}'.format(tu['data']))
    resp = int(Request().req(tu['url'], tu['method'], eval(tu['data']), login).json()['code'])
    try:
        assert resp == int(tu['code'])
        log.info('用例成功，响应code码为：{}'.format(resp))
    except AssertionError as e:
        log.error('用例失败{}'.format(e))
