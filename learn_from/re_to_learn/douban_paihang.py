from os import pardir
import requests
import re
import csv
import time
#构造网页头
url='https://movie.douban.com/top250'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
numbers=0
while (numbers<=100):
    pardom={
        'start': numbers,
        'filter': '',
    }
    #获取网页代码
    resp=requests.get(url,headers=headers,params=pardom)
    page_content=resp.text
    #解析数据
    obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
        r'</span>.*?<br>(?P<year>.*?)&nbsp.*?<span '
        r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
        r'<span>(?P<number>.*?)评价</span>',re.S)
    result=obj.finditer(page_content)
    f=open("data.csv",'a+',encoding='utf-8',newline='')
    csvwriter=csv.writer(f)
    for it in result:
        dic=it.groupdict()
        dic['year']=dic['year'].strip()
        csvwriter.writerow(dic.values())
    f.close()
    numbers+=25
    time.sleep(2)

print('Over')