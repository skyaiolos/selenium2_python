# coding=utf-8
__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        第二节、python  多进程/ 线程基础
在使用多线程之前，我们首页要理解什么是进程和线程。
什么是进程？
计算机程序只不过是磁盘中可执行的，二进制（或其它类型）的数据。它们只有在被读取到内存中，
被操作系统调用的时候才开始它们的生命期。进程（有时被称为重量级进程）是程序的一次执行。每个进
程都有自己的地址空间，内存，数据栈以及其它记录其运行轨迹的辅助数据。操作系统管理在其上运行的
所有进程，并为这些进程公平地分配时间。
什么是线程？
线程（有时被称为轻量级进程）跟进程有些相似，不同的是，所有的线程运行在同一个进程中，共享
相同的运行环境。我们可以想像成是在主进程或“主线程”中并行运行的“迷你进程”。

8.2.1 、 单线程
在单线程中顺序执行两个循环。一定要一个循环结束后，另一个才能开始。总时间是各个循环
运行时间之和。
"""

from time import sleep, ctime

"""
8.2.1 、 单线程
在单线程中顺序执行两个循环。一定要一个循环结束后，另一个才能开始。总时间是各个循环
运行时间之和。
"""
def loop0():
    print(' start loop 0 at: %s' % ctime())
    sleep(4)
    print(' loop 0 done at: %s' % ctime())


def loop1():
    print(' start loop 1 at: %s' % ctime())
    sleep(2)
    print(' loop 1 done at: %s' % ctime())


def main():
    print('start: %s' % ctime())
    loop0()
    loop1()
    print('All end: %s' % ctime())


if __name__ == '__main__':
    main()

# start: Mon Jul 24 12:51:25 2017
#  start loop 0 at: Mon Jul 24 12:51:25 2017
#  loop 0 done at: Mon Jul 24 12:51:29 2017
#  start loop 1 at: Mon Jul 24 12:51:29 2017
#  loop 1 done at: Mon Jul 24 12:51:31 2017
# All end: Mon Jul 24 12:51:31 2017
"""
    Description:
        Python 通过两个标准库 thread 和 threading 提供对线程的支持。thread 提供了低级别的、原始的
线程以及一个简单的锁。threading 基于 Java 的线程模型设计。锁（Lock）和条件变量（Condition）
在 Java 中是对象的基本行为（每一个对象都自带了锁和条件变量），而在 Python 中则是独立的对象。
"""
