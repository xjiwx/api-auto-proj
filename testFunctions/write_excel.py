import requests

s = requests.Session()
#登录接口
res = s.post(url="http://novel.hctestedu.com/user/login",data={'username':'17701293276','password':'123456'}) # 用户名和密码填自己的
# 获取cookie(字典格式)
cookiejar = res.cookies.get_dict()
print('最初的cookie:',cookiejar)
x = res.json()
print('返回值里有token:',res.json())
print('token的值:',x['data']['token'])
cookiejar['Authorization'] = x['data']['token']
print('加上token之后的cookie:',cookiejar)
# 把字典变成一个键值对用'='相连，不同键值对用';'隔开 的字符串
cookie_string = ';'.join(str(x)+ '='+ str(y) for x,y in cookiejar.items())
headers = {
    'Cookie': cookie_string
}
#书架接口
booklist = requests.get('http://novel.hctestedu.com/user/listBookShelfByPage?curr=1&limit=10',headers= headers)
print('书架列表:',booklist.text)

