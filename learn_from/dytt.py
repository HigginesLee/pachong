import re
import requests
#请求主页面
url='https://dytt89.com'
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
}
resp=requests.get(url,headers=headers)
resp.encoding='gb2312'#转码
#正则
#分析主页面
obj=re.compile(r'2021必看热片.*?<ul>(?P<URL>.*?)</ul>',re.S)
#获得“必看热片”的url地址与标题
obj1=re.compile(r"<li><a href='(?P<ul>.*?)' title=.*?>(?P<title>.*?)</a>",re.S)
obj2=re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)


result=obj.finditer(resp.text)
child_herf_list=[]
for it in result:
    ul=it.group('URL')
result1=obj1.finditer(ul)
for item in result1:
    child_herf_list.append(item.group('ul'))

#提取子页面内容
for href in child_herf_list:
    child_resp=requests.get(url=url+href,headers=headers)
    child_resp.encoding='gb2312'
    result2=obj2.search(child_resp.text)
    print(result2.group('movie'),result2.group('download'))