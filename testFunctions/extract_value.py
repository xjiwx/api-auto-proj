class extract:
    @classmethod
    def dict_atuple(self,lis):
        at = []
        for i in lis:
            print(type(i))
            for k in i.values():
                at.append(k)


        return at
list = [{'rowNum': 2, 'description': 'login success', 'url': 'http://novel.hctestedu.com/user/login', 'method': 'post', 'data': "{'username': '17701293276', 'password': '123456'}", 'cookie': 'None', 'code': '200', 'response': 'token', 'result': ''},
{'rowNum': 3, 'description': 'abnormal password', 'url': 'http://novel.hctestedu.com/user/login', 'method': 'post', 'data': "{'username': '17701293276', 'password': ''}", 'cookie': 'None', 'code': '1004', 'response': "{'code': '1004', 'msg': '手机号或密码错误！', 'data': None}", 'result': ''},
{'rowNum': 4, 'description': 'abnormal username', 'url': 'http://novel.hctestedu.com/user/login', 'method': 'post', 'data': "{'username': '', 'password': '123456'}", 'cookie': 'None', 'code': '1004', 'response': "{'code': '1004', 'msg': '手机号或密码错误！', 'data': None}", 'result': ''}
]
print(tuple(list))

