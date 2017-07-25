# coding=utf-8
__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        这一章将详细的讲解基于 python 的 webdriver API,笔者更愿意读者自已去查询 webdriver API 中各
种操作方法的使用，为了保持本书由浅入深的完整性，本章将用相当有篇幅介绍基于 python 语言的
webdriver 对种操作的使用。通过本章的学习，我们掌握 web 页面上各种元素、弹窗的定位与操作，以及
浏览器 cookie 的操作，JavaScript 的调用等问题。
第一节、浏览器的操作
3. 1.1 浏览器最大化。
"""
from selenium import webdriver
import time, os

try:
    if not os.path.exists("./Captures"):
        Captures_folder = os.mkdir("./Captures")

except OSError:
    pass

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()  # 将浏览器最大化显示
time.sleep(2)
driver.get_screenshot_as_file('./Captures/maxWindow.png')
driver.quit()
