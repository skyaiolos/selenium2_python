# coding=utf-8
__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        3.1.3 、控制浏览器前进、后退
浏览器上有一个后退、前进按钮，对于浏览网页的人是比较方便的；对于 web 自动化测试来说是
一个比较难模拟的操作；webdriver 提供了 back()和 forward()方法，使实现这个操作变得非常简单。
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://m.mail.10086.cn")

second_url = 'http://news.baidu.com'

print("now access the 2nd url %s" % second_url)
driver.get(second_url)
driver.get_screenshot_as_file("./Captures/baidu.png")

print("back to mail.10086")
driver.back()
driver.get_screenshot_as_file("./Captures/mail10086.png")

driver.forward()
driver.get_screenshot_as_file("./Captures/baidu_again.png")

if __name__ == '__main__':
    pass
