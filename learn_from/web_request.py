#user HigginesLee
#date 2022-1-7
'''
1.服务器渲染:在服务器把HTML和数据聚合在一起，统一返回浏览器
2.客户端渲染:第一次请求只要HTML骨架，第二次请求数据，进行数据显示。在页面代码中看不到数据
熟练使用浏览器抓包工具
熟练使用抓包工具
'''
import requests
url='https://www.sogou.com/web?query=周杰伦'
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
}
response=requests.get(url,headers=headers)
print(response.text)