import asyncio
import aiohttp
import aiofiles
urls=[
    'http://kr.shanghai-jiuxin.com/file/2021/0616/947ca58d7d8f08c36c16d62192249ab7.jpg',
    'http://kr.shanghai-jiuxin.com/file/2021/0616/c43c448f13ea9be3522f30942462f3c3.jpg',
    'http://kr.shanghai-jiuxin.com/file/2021/0616/39e15a1c5218b2e80135ee6afb31fb37.jpg'
]
async def download(url):
    name=url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:#<====>requests
        async with session.get(url) as rep:
            async with aiofiles.open(name,mode="wb")as f:#或者使用aiofiles
                await f.write(await rep.content.read())
    print(name,"搞定")
async def main():
    tasks=[]
    for url in urls:
        d=asyncio.create_task(download(url))
        tasks.append(d)
    await asyncio.wait(tasks)

if __name__=='__main__':
    #asyncio.run(main())#会有RuntimeErrot报错
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())