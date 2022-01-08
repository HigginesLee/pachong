#user HigginesLee
#date 2022-1-7
import requests
url='https://fanyi.baidu.com/sug'
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
}
s=input("请输入你要翻译的单词：")
dat={
    'kw':s
}
resp=requests.post(url,data=dat)
print(resp.json())