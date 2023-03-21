import json
import jsonpath
import requests
# from common.Logger import logger


class ApiKey:
    def __init__(self):
        # 定义一个字典用于保存处理后的接口返回值
        self.all_val = {}

    # 用于提取返回结果中所需要的内容
    def get_text(self, data, key):

        # loads将json格式数据转换为字典格式
        dict_data = json.loads(data)

        try:
            value_list = jsonpath.jsonpath(dict_data, key)
            # 返回的是列表,取列表第一个值
            return value_list[0]
        except:
            return '查询失败,没有找到key值{}'.format(key)

    def save_json(self, data, name, key):
        dict_data = json.loads(data)
        try:
            value = jsonpath.jsonpath(dict_data, key)[0]
            self.all_val[name] = value
        except:
            return '保存json失败,没有找到key值{}'.format(key)

    # get请求的封装
    def get(self, url, params=None, **kwargs):
        res = requests.get(url, params=params, **kwargs)
        return res

    # post请求的封装
    def post(self, **kwargs):
        res = requests.post(**kwargs)
        return res