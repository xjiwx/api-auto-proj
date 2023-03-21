import requests

class Request:
    def req(self,url, method, data=None, headers=None):
        s = requests.Session()
        if method.lower() == 'get':  # 防止大小写写错
            res = s.get(url, params=data, headers=headers)
        else:
            res = s.post(url,data, headers=headers)
        return res



