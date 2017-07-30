__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/29
"""
    Description:
       .1.3 数据驱动
    txt 文件是我们经常操作的文集类型，Python提供了一下几种读取txt文件的方式.
1.  read():  读取整个文件
2.  readline():  读取一行数据
3.  readlines():    读取所有行的数据。

user_info.txt
张三,123
李四,456
王五,789
"""

from selenium import webdriver
import time

with open('user_info.txt', 'r', encoding="utf-8") as user_file:
    lines = user_file.readlines()
    user_file.close()

for line in lines:
    username = line.split(',')[0]
    pwd = line.split(',')[1]
    print("UserName: {} \nPassword: {}".format(username, pwd))
