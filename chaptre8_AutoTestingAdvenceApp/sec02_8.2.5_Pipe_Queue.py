# coding=utf-8
__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
       8.2.5 、e Pipe 和 和  queue
multiprocessing 包中有 Pipe 类和 Queue 类来分别支持这两种 IPC 机制。Pipe 和 Queue 可以
用来传送常见的对象。
（ 1 ） Pipe 可 以 是 单 向 (half-duplex) ， 也 可 以 是 双 向 (duplex) 。 我 们 通 过
mutiprocessing.Pipe(duplex=False)创建单向管道 (默认为双向)。一个进程从 PIPE 一端输入
对象，然后被 PIPE 另一端的进程接收，单向管道只允许管道一端的进程输入，而双向管道则允许从两端
输入。
pipe.py 
"""
import multiprocessing


def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:', pipe.recv())


def proc2(pipe):
    print('proc2 rec:', pipe.recv())
    pipe.send('hello, too')


pipe = multiprocessing.Pipe()
p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))

p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))
p1.start()
p2.start()
p1.join()
p2.join()

# 注：本程序只能在 linux/Unix 上运行，运行结果
# ‘proc2 rec:’，‘hello’
# ‘proc2 rec:’，‘hello,too’