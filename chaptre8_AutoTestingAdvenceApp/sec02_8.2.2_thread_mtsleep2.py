# coding=utf-8
__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        8.2.2 、thread 
"""

import _thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec, lock):
    print(' start loop', nloop, 'at: %s' % ctime())
    sleep(nsec)
    print(' loop', nloop, 'done at: %s' % ctime())

    # 解锁
    # lock.release()


def main():
    print('start: %s' % ctime())
    locks = []
    # 以 loops 数组创建列表，并赋值给 nloops
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        # 锁定
        lock.acquire()

        # 追加到locks[]数组中
        locks.append(lock)

    # 执行多线程
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[1]))

    for i in nloops:
        while locks[i].locked():
            pass

    print('all end: %s' % ctime())


if __name__ == '__main__':
    main()
""" 
    Result:
    start_new_thread()要求一定要有前两个参数。所以，就算我们想要运行的函数不要参数，我们也
要传一个空的元组。
这个程序的输出与之前的输出大不相同，之前是运行了 6，7 秒，而现在则是 4 秒，是最长的循环
的运行时间与其它的代码的时间总和。

"""
# start: Mon Jul 24 13:01:27 2017
#  start loop 1 at: Mon Jul 24 13:01:27 2017
#  start loop 0 at: Mon Jul 24 13:01:27 2017
#  loop 1 done at: Mon Jul 24 13:01:29 2017
#  loop 0 done at: Mon Jul 24 13:01:31 2017
# All end: Mon Jul 24 13:01:33 2017

"""
    睡眠 4 秒和 2 秒的代码现在是并发执行的。这样，就使得总的运行时间被缩短了。你可以看到，
loop1 甚至在 loop0 前面就结束了。
程序的一大不同之处就是多了一个“sleep(6)”的函数调用。如果我们没有让主线程停下来，那主线
程就会运行下一条语句，显示“all end”，然后就关闭运行着 loop0()和 loop1()的两个线程并退出了。
"""
