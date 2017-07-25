# coding=utf-8
__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        8.2.4 、g multiprocessing  模块
multiprocessing 使用类似于 threading 模块的 API ，multiprocessing 提供了本地和远程的并发性，有
效的通过全局解释锁(Global Interceptor Lock, GIL)来使用进程(而不是线程)。由于 GIL 的存在，在 CPU 密
集型的程序当中，使用多线程并不能有效地利用多核 CPU 的优势，因为一个解释器在同一时刻只会有一
个线程在执行。所以，multiprocessing 模块可以充分的利用硬件的多处理器来进行工作。它支持 Unix 和
Windows 系统上的运行。
process1.py
"""
from multiprocessing import Process


def f(name):
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
"""
与 threading.Thread 类似，它可以利用 multiprocessing.Process 对象来创建一个进程。Process 对象与
Thread 对象的用法相同，也有 start(), run(), join()的方法。
multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})
target 表示调用对象，args 表示调用对象的位置参数元组。kwargs 表示调用对象的字典。Name 为别名。
Group 实质上不使用。
"""