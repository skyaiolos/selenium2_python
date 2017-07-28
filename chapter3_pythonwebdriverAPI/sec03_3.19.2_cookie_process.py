__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/28
"""
    Description:
        第十九节 cookie  处理
有时候我们需要验证浏览器中是否存在某个 cookie，因为基于真实的 cookie 的测试是无法通过白盒
和集成测试完成的。webdriver 可以读取、添加和删除 cookie 信息。
webdriver 操作 cookie 的方法有：
1.  get_cookies() 获得所有 cookie 信息
2.  get_cookie(name) 返回特定 name 有 cookie 信息
3.  add_cookie(cookie_dict) 添加 cookie，必须有 name 和 value 值
4.  delete_cookie(name) 删除特定(部分)的 cookie 信息
5.  delete_all_cookies() 删除所有 cookie 信息
通过 webdriver 操作 cookie 是一件非常有意思的事儿，有时候我们需要了解浏览器中是否存在了某个
cookie 信息，webdriver 可以帮助我们读取、添加，删除 cookie 信息。
1 3.19.1  打印 e cookie  信息
"""
from selenium import webdriver
import time
from pprint import pprint

driver = webdriver.Chrome()

driver.get("http://www.youdao.com")

# 向 cookie 的 name 和 value 添加会话信息。
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbb'})

# 遍历 cookies 中的 name 和 value 信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

##### 下面可以通过两种方式删除 cookie #####
# 删除一个特定的 cookie
driver.delete_cookie("CookieName")
# 删除所有 cookie
driver.delete_all_cookies()
time.sleep(2)
driver.close()
