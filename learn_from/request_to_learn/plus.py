#使用requests处理cookie
#可以使用session进行请求,可以认为是一连串的请求，在这个过程中cookie不会吊事

import requests
#会话
session=requests.session()
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
data={
'loginName': '18614075987',
'password': 'q6035945'
}
#1.登录
url='https://passport.17k.com/ck/user/login'
session.post(url,headers=headers,data=data)
#2.拿数据
# print(resp.cookies)
url2='https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
resp=session.get(url2)
print(resp.json())

