import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from random import randint
url = 'https://www.umei.cc/meinvtupian/meinvxiezhen/'
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
}
resp=requests.get(url,headers=headers)
resp.encoding='utf-8'#处理乱码
main_page=bs(resp.text,'html.parser')
alist=main_page.find("div",class_="TypeList").find_all("a")
for a in alist:
    herf=url+a.get('href')[25:]
    child_resp=requests.get(herf,headers=headers)
    child_resp.encoding='utf-8'
    child_page=bs(child_resp.text,"html.parser")
    cl=child_page.find("div",class_="ImageBody")
    img=cl.find("img")
    src=img.get("src")
    img_resp=requests.get(src)
    img_name="./picture/"+src.split('/')[-1]
    with open(img_name,'wb') as f:
        f.write(img_resp.content)#返回的是字节
    print(img_name,"Over")
    sleep(randint(1,3))
print('ALL Successful')