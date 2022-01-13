'''
流程:
1.访问HTML，获取源代码
2.下载m3u8的url
3.读取m3u8
4.合并视频
'''
from os import write
import requests
import re
obj=re.compile(r"url: '(?P<url>.*?)',",re.S)#用来提取m3u8的地址
url='https://www.91kanju.com/vod-play/61282-1-38.html'
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36',
}
resp=requests.get(url,headers=headers)
m3u8_url=obj.search(resp.text).group("url")
resp.close()
#下载m3u8
resp2=requests.get(m3u8_url,headers=headers)

with open("./picture/雪中悍刀行.m3u8",mode='wb') as f:
    f.write(resp2.content)
resp2.close()
print("Success")

n=1
#解析m3u8文件
with open('./picture/雪中悍刀行.m3u8','r',encoding='utf-8') as f:
    for line in f:
        line=line.strip()
        if line.startswith("#"):#过滤以#号开头的无用文件
            continue
        #下载片段
        resp3=requests.get(line,headers=headers)
        f=open(f"./picture/{n}.ts",'wb')
        f.write(resp3.content)
        f.close()
        resp3.close()
        n+=1