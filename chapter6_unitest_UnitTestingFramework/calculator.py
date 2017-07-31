__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        计算器
"""
#计算器类
class Count():
    def __init__(self,a ,b):
        self.a = int(a)

        self.b = int(b)

    #计算加法

    def add(self):
        c = self.a +self.b
        return c

    def sub(self):
        c = self.a -self.b
        return c







