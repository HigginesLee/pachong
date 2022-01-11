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
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def func(name):
    for i in range(10):
        print(name,i)

if __name__=='__main__':
    #创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(func,name=f'线程{i}')
    #等待线程中的任务执行完毕才会继续执行(守护)
    print('123')