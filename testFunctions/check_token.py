from testFunctions.read_excel import ExcelUtil
from testFunctions.request import Request

class Token(Request):
    def get_token(self):
        res = Request().request(url="http://novel.hctestedu.com/user/login",method= 'post',data={'username': '17701293276', 'password': '123456'})  # 用户名和密码填自己的
        cookiejar = res.cookies.get_dict()
        x = res.json()
        cookiejar['Authorization'] = x['data']['token']
        # 把字典变成一个键值对用'='相连，不同键值对用';'隔开 的字符串
        cookie_string = ';'.join(str(x) + '=' + str(y) for x, y in cookiejar.items())
        headers = {
            'Cookie': cookie_string
        }

        return headers


#
t = Token()
print(t.get_token())