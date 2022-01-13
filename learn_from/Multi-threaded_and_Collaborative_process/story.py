
import aiofiles
import asyncio
import aiohttp
import requests
import json
'''
1.同步访问getCatalog拿到cid
2.异步访问下载内容
'''
async def getCatalog(url,headers=None):
    tasks=[]
    resp=requests.get(url,headers=headers)
    dic=resp.json()
    for item in dic['data']['novel']['items']:
        title=item['title']
        cid=item['cid']
        d=asyncio.create_task(download(cid,b_id,title))
        tasks.append(d)
    await asyncio.wait(tasks)
        
async def download(cid,b_id,title):
    data={
    "book_id":b_id,
    "cid":f"{b_id}|{cid}",
    "need_bookinfo":1}
    data=json.dumps(data)
    url=f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url)as resp:
            dic=await resp.json()
            async with aiofiles.open(f"./xiyou/{title}.txt",'w',encoding='utf-8')as f:
                await f.write(dic['data']['novel']['content'])
                print(title,"Over")
if __name__=='__main__':
    b_id="4306063500"
    url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+b_id+'"}'
    headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36',
        'Referer':f'https://dushu.baidu.com/pc/detail?gid={b_id}'
    }
    loop=asyncio.get_event_loop()
    loop.run_until_complete(getCatalog(url,headers))