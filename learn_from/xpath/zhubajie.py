import requests
from lxml import etree
def get(ul):
    url=ul
    headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    main_page=response.text
    return main_page
url='https://haerbin.zbj.com/search/f/?type=new&kw=saas'
main_page=get(url)
html=etree.HTML(main_page)
#拿到每一个服务商的div
divs=html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
for div in divs:
    com_name=div.xpath("./div/div/a[1]/div[1]/p/text()")[1].replace('\n','')
    price=div.xpath("./div/div/a/div[2]/div/span[@class='price']/text()")[0]
    title='saas'.join(div.xpath("./div/div/a/div[2]/div[2]/p/text()"))
    zone=div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
    print(title)

    
