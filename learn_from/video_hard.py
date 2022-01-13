import requests
import re
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES
import os
'''
页面源码，写re用
# <script>var vid="705";var vfrom="1";var vpart="0";
# var now="https://video.dious.cc/20200825/9qvL6V78/index.m3u8";var pn="yunbo2"; 
# var next="https://video.dious.cc/20200825/hdOEspOx/index.m3u8";
# var prePage="/play/705-1-0.html";var nextPage="/play/705-1-1.html";</script>
'''
obj=re.compile(r'<script>.*?var now="(?P<now_url>.*?)".*?var nextPage="(?P<next_page>.*?)"',re.S)
#获取ifram中的url地址----美剧天堂源代码中直接返回的就是url地址，本处仅仅是根据老师按照91看剧步骤写的
#正常可以直接返回Url地址获取m3u8文件，即调用
def get_iframe_src(url,headers=None):
    resp=requests.get(url,headers=headers)
    now_url=obj.search(resp.text).group("now_url")
    resp.close()
    return now_url
#根据ifram中的代码获取视频的第一层的m3u8文件地址
def get_first_m3u8_url(url,headers=None):
    resp=requests.get(url,headers=headers)
    m3u8_url=obj.search(resp.text).group("now_url")
    resp.close()
    return m3u8_url

def download_m3u8_files(url,name,headers=None):
    resp=requests.get(url,headers)
    with open(f'./video/{name}','wb')as f:
        f.write(resp.content)

async def download_ts(url,name,session,headers=None):
    async with session.get(url)as resp:
        async with aiofiles.open(f"./video2/{name}",mode="wb") as f:
            await f.write(await resp.content.read())
    print(name,"下载完毕")
async def aio_download(headers=None):
    tasks=[]
    async with aiohttp.ClientSession()as session:
        async with aiofiles.open("./video/dushi_2.m3u8",mode="r") as f :
            async for line in f:
                if line.startswith('#'):
                    continue
                else:
                    line=line.strip()
                    task=asyncio.create_task(download_ts(line,line.rsplit("/",1)[1],session,headers))#创建任务
                    tasks.append(task)
            await asyncio.wait(tasks)

def get_key(url):
    resp=requests.get(url)
    return resp.text

async def dec_ts(name,key):
    aes=AES.new(key=key,IV=b'0000000000000000',mode=AES.MODE_CBC)
    async with aiofiles.open(f"./video2/{name}","rb")as f1,\
        aiofiles.open(f"./video2/temp_{name}","wb")as f2:
        bs=await f1.read()#从源文件读取内容
        await f2.write(aes.decrypt(bs))#解密文件
    print(f"{name}处理完毕")

def merge_ts():
    lst=[]
    with open("./video/dushi_2.m3u8",'r',encoding='utf-8')as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line=line.strip().rsplit("/",1)[1]
                lst.append(f"./video2/temp_{line}")
    s=" ".join(lst)#linux
    os.system(f"cat {s}>movie.mp4")
    # s="+^".join(lst)
    # os.system(f"copy \\b {s} > movie.mp4")
    print("搞定")



async def aio_dec(key):
    tasks=[]
    async with aiofiles.open("./video/dushi_2.m3u8",mode="r",encoding="utf-8")as f:
        async for line in f:
            if line.startswith("#"):
                continue
            else:
                line=line.strip().rsplit("/",1)[1]
                task=asyncio.create_task(dec_ts(line,key))
                tasks.append(task)
        await asyncio.wait(tasks)
def main(url,headers=None):
    #1.获得iframe的视频地址
    iframe_src=f'https://www.ttjj.cc/js/dp.php?v={get_iframe_src(url,headers)}'
    #2.拿到第一层m3u8文件的下载地址
    first_m3u8_url=get_first_m3u8_url(url,headers)
    #3.下载第一层m3u8文件
    # download_m3u8_files(first_m3u8_url,"dushi.m3u8",headers=headers)
    #4.下载第二层m3u8文件
    with open("./video/dushi.m3u8","r",encoding="utf-8")as f:
        for line in f:
            if(line.startswith("#")):
                continue
            else:
                line=line.strip()
                second_url=first_m3u8_url.rsplit("/",3)[0]+line
                download_m3u8_files(second_url,"dushi_2.m3u8",headers=headers)
                print("m3u8下载完成")
    #5.异步下载ts文件
    loop=asyncio.get_event_loop()
    # #此处与老师讲的案例有不同，老师的是文件中没有完整的url地址，需要替换出url前一致的地方并传入，然后得到完整的Url地址，而美剧天堂是完整的url地址，顾不需要传参
    loop.run_until_complete(aio_download(headers))
    #6.拿到密钥
    #正常是需要读取m3u8文件
    key_url=f'https://ts1.tkzyapi1.com/20200825/9qvL6V78/1000kb/hls/key.key'
    key=get_key(key_url)
    key=key.encode('utf-8')
    #7.解密---异步协程
    loop2=asyncio.get_event_loop()
    loop2.run_until_complete(aio_dec(key))
    #合并ps4文件
    merge_ts()
if __name__=='__main__':
    url='https://www.ttjj.cc/play/705-1-0.html'
    headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36',
    }
    main(url,headers=headers)