# coding=utf-8
__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        使用可调用的类
mtsleep4.py
"""
import threading
from time import sleep, ctime

loops = [4, 2]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

        # def __call__(self):
        #     apply(self.func, self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at: %s' % ctime())
    sleep(nsec)
    print('loop', nloop, 'done at: %s' % ctime())


def main():
    print('starting at: %s' % ctime())
    threads = []
    nloops = range(len(loops))

    # 创建线程
    for i in nloops:
        # 调用ThreadFunc 实例化的对象，创建所有线程
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    # 开始线程
    for i in nloops:
        threads[i].start()

    # 等待所有结束线程
    for i in nloops:
        threads[i].join()

    print('all end: %s ' % ctime())


if __name__ == '__main__':
    main()
"""
start()
开始线程活动
join()
等待线程终止
所有的线程都创建了之后，再一起调用 start()函数启动，而不是创建一个启动一个。而且，不用再
管理一堆锁（分配锁，获得锁，释放锁，检查锁的状态等），只要简单地对每个线程调用 join()函数就可
以了。
join()会等到线程结束，或者在给了 timeout 参数的时候，等到超时为止。join()的另一个比较重
要的方面是它可以完全不用调用。一旦线程启动后，就会一直运行，直到线程的函数结束，退出为止。
"""
# starting at: Mon Jul 24 13:31:15 2017
#  start loop 0 at: Mon Jul 24 13:31:15 2017
#  start loop 1 at: Mon Jul 24 13:31:15 2017
#  loop 1 done at: Mon Jul 24 13:31:17 2017
#  loop 0 done at: Mon Jul 24 13:31:19 2017
# all end: Mon Jul 24 13:31:19 2017
