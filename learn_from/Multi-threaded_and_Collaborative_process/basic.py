#多线程（异步）
from threading import Thread
#传参必须是元组
# def func():
#     for i in range(1000):
#         print("func",i)
# if __name__=='__main__':
#     t=Thread(target=func)
#     t.start()
#     for i in range(1000):
#         print("main",i)
# class MyThread(Thread):
#     def run(self):
#         for i in range(1000):
#             print("子线程",i)     
# if __name__=='__main__':
#     t=MyThread()
#     t.start()
#     for i in range(1000):
#         print("主线程",i)   

#多进程
# from multiprocessing import Process
# def func():
#     for i in range(1000):
#         print("子进程",i)
# if __name__=='__main__':
#     t=Process(target=func)
#     t.start()
#     for i in range(1000):
#         print("主进程",i)

#线程池：一次性开辟一些线程，用户直接个线程池提交任务，线程任务调度交给线程池来完成
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def func(name):
#     for i in range(10):
#         print(name,i)

# if __name__=='__main__':
#     #创建线程池
#     with ThreadPoolExecutor(50) as t:
#         for i in range(100):
#             t.submit(func,name=f'线程{i}')
#     #等待线程中的任务执行完毕才会继续执行(守护)
#     print('123')

#单线程操作系统
# 阻塞状态，当程序处于IO状态时，线程处于阻塞状态
#协程：当程序遇见IO操作，可以选择性的切换到其他任务上
#在微观上是一个任务一个进行切换，切换条件一般是IO操作
#宏观上是多个任务一起执行
#多任务异步操作

#python 编写协程的程序
import asyncio
import time
# async def func():
#     print("llalalaal")
# async def func3():#async代表协程
#     print("你好啊！我叫赛利亚")
#     #time.sleep(3)
#     await asyncio.sleep(3)#异步操作代码
#     print("33333")
# async def func1():
#     print("潘金莲")
#     #time.sleep(1)
#     await asyncio.sleep(1)
#     print("111")
# async def func2():
#     print("王建国")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("2222")

# if __name__=='__main__':
#     # g=func()#此时的函数是异步协程函数，此时函数执行的是一个协程对象
#     # asyncio.run(g)#协程程序运行需要asyncio模块
#     f1=func1()
#     f2=func2()
#     f3=func3()
#     task=[
#         f1,f2,f3
#     ]
#     t1=time.time()
#     #一次性启用多个协程
#     asyncio.run(asyncio.wait(task))
#     t2=time.time()
#     print(t2-t1)

# async def func3():#async代表协程
#     print("你好啊！我叫赛利亚")
#     await asyncio.sleep(3)#异步操作代码
#     print("33333")
# async def func1():
#     print("潘金莲")
#     await asyncio.sleep(1)
#     print("111")
# async def func2():
#     print("王建国")
#     await asyncio.sleep(2)
#     print("2222")

# async def mian():
#     #第一种写法
#     #f1=func1()
#     #await f1   #await在协程对象前
#     #第二种写法
#     task=[
#         asyncio.create_task(func1()),
#         asyncio.create_task(func2()),
#         asyncio.create_task(func3())
#     ]#新版本的要求
#     await asyncio.wait(task)

# if __name__=='__main__':
#     t1=time.time()
#     asyncio.run(mian())
#     t2=time.time()
#     print(t2-t1)

async def download(url):
    print("准备开始下载")
    await asyncio.sleep(3)
    print("下载完成")
async def main():
    urls=[
        "https://www.baidu.com",
        "https://www.bilibili.com",
        "https://www.163.com",
    ]
    tasks=[]
    for url in urls:
        d=download(url)
        tasks.append(asyncio.create_task(d))
    await asyncio.wait(tasks)
if __name__=='__main__':
    asyncio.run(main())