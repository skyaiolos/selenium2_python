# coding=utf-8
__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        基于继承的对象共享的基础。所谓基于继承的对象共享，是说在创建子进程之前由父进程初始化的某些对
象可以在子进程当中直接访问到。在 Windows 平台上，因为没有 fork 语义的系统调用，基于继承的共
享对象比*nix 有更多的限制，最主要就是体现在要求 Process 的__init__当中的参数必须可以 Pickle。
但是，并不是所有的对象都是可以通过继承来共享，只有 multiprocessing 库当中的某些对象才可以。
例如 Queue，同步对象，共享变量，Manager 等等。
在一个 multiprocessing 库的典型使用场景下，所有的子进程都是由一个父进程启动起来的，这个父
进程称为 master 进程。这个父进程非常重要，它会管理一系列的对象状态，一旦这个进程退出，子进程
很可能会处于一个很不稳定的状态，因为它们共享的状态也许已经被损坏掉了。因此，这个进程最好尽可
能做最少的事情，以便保持其稳定性。
process2.py
"""
from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name: %s' % __name__)
    if hasattr(os, 'getppid'):
        print('parent process: %s' % os.getpid())
    print('process id: %s' % os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
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
#
# main line
# module name: __main__
# parent process: 11300
# process id: 11300
# function f
# module name: __mp_main__
# parent process: 14212
# process id: 14212
# hello bob
"""
    multiprocessing 提供了 threading 包中没有的 IPC(比如 Pipe 和 Queue)，效率上更高。应优先
考虑 Pipe 和 Queue，避免使用 Lock/Event/Semaphore/Condition 等同步方式 (因为它们占据的不
是用户进程的资源)。
hasattr(object, name)
判断对象 object 是否包含名为 name 的特性（hasattr 是通过调用 getattr(ojbect, name)是否抛出异常来实
现的）。hasattr(os, 'getppid') 用于判断系统是否包含 getppid。
getpid()得到本身进程 id，getppid()得到父进程进程 id，如果已经是父进程，得到系统进程
id。
Process.PID 中保存有 PID，如果进程还没有 start()，则 PID 为 None。
"""
