__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/27
"""
    Description:
        第十五节 上传文件
文件上传操作也比较常见功能之一，上传功能操作 webdriver 并没有提供对应的方法，关键上传文
件的思路。
上传过程一般要打开一个系统的 window 窗口，从窗口选择本地文件添加。所以，一般会卡在如何操
作本地 window 窗口。其实，上传本地文件没我们想的那么复杂；只要定位上传按钮，通 send_keys 添加
本地文件路径就可以了。绝对路径和相对路径都可以，关键是上传的文件存在。下面通地例子演示操作过
程。
upload_file.html
"""
from selenium import webdriver

import time, os

driver = webdriver.Chrome()
upfile = 'file:///' + os.path.abspath("upload_file.html")
driver.get(upfile)
driver.find_element_by_name("file").send_keys("./baidu_logon.png")
time.sleep(3)
driver.quit()
