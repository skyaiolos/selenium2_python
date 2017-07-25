# coding=utf-8
__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        第三节、多进程执行测试用例
因为多进程与多线程特性在 python 中当中也属于比较高级的应用，对于初学者来说比理解起来有一定
难度，所以在介绍 python 的多进程与多线程时我们通过相当的篇幅和实例来进行讲解，目的是为了让读
者深入的理解 python 的多进程与多线程。
为实现多进程运行测试用例，我需要对文件结构进行调整：
/selenium_proces/thread1/start_baidu.py -----测试用例
/thread1/__init__.py
/thread2/start_youdao.py -----测试用例
/thread2/__init__.py
/all_tests_process.py
我们创建了thread1和thread2两个文件夹，分别放入了两个测试用例；下面我们编写all_tests_process.py
文件来通过多进程来执行测试用例。

"""
import unittest,time,os,multiprocessing
# import commands
from email.mime.text import MIMEText
import HTMLTestRunner
import sys

def EEEcreatsuite1():
    casedir = []
    listaa=os.listdir(r'D:\Demo_python\selenium_process')


if __name__ == '__main__':
    pass

