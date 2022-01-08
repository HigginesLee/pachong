from bs4 import BeautifulSoup as bs
import requests
import csv
f=open('price.csv','w',encoding='utf-8')
csv_writer=csv.writer(f)
#拿到源代码
#解析
url='http://www.xinfadi.com.cn/priceDetail.html'
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
}
resp=requests.post(url,headers=headers)
page=bs(resp.text,"html.parser")
#find(标签,属性=值)
#find_all(标签,属性=值)
#如果与关键字冲突，可以在名字后面加_
#或者attrs={"标签名":"值"}
table=page.find("table",attrs={'class':'hq_table'})
trs=table.find_all("tr")[1:]

for tr in trs:
    tds=tr.find_all("td")#拿到每行中的所有td
    name=tds[0].text
    low=tds[1].text
    avg=tds[2].text
    high=tds[3].text
    gui=tds[4].text
    kind=tds[5].text
    date=tds[6].text
    csv_writer.writerow(name,low,avg,high,gui,kind,date)
resp.close()
f.close()
print("Over")