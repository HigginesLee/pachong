#代理
#原理：通过第三方发送数据请求
import requests
import time
from lxml import etree
# 222.190.163.192:9001
proxies={
    'https:':'',
}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}
def get(ul,headers=headers,proxies=None):
    url,head,proxie=ul,headers,proxies
    start_time=time.time()
    resp=requests.get(url,headers=head,proxies=proxie)
    end_time=time.time()
    page=etree.HTML(resp.text)
    ip_addr=page.xpath("/html/body/div[2]/div[@id='bdy']/div[1]/div[1]/div[1]/form/p/text()")[0]
    return ip_addr,end_time-start_time
url='https://tool.lu/ip/'
ip_addr1,time1=get(url)
ip_addr2,time2=get(url,proxies=proxies)
print(ip_addr1,"\n所用时间为",time1)
print(ip_addr2,"\n所用时间为",time2)