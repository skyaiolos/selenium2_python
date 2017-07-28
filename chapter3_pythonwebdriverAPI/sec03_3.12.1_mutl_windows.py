__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/28
"""
    Description:
        第十二节 浏览器多窗口处理
有时候我们在测试一个 web 应用时会出现多个浏览器窗口的情况，在 selenium1.0 中这个问题比较难
处理。webdriver 提供了相关相方法可以很轻松的在多个窗口之间切换并操作不同窗口上的元素。
要想在多个窗口之间切换，首先要获得每一个窗口的唯一标识符号（句柄）。通过获得的句柄来区别
分不同的窗口，从而对不同窗口上的元素进行操作。

"""
from selenium import webdriver
import time, os

driver = webdriver.Chrome()

driver.get("https://tieba.baidu.com/index.html")
driver.maximize_window()
driver.implicitly_wait(5)

# get current window handle

nowhandle = driver.current_window_handle

# 打开注册新窗口
driver.find_element_by_css_selector(".u_reg > div:nth-child(1) > a:nth-child(1)").click()
# driver.find_element_by_name('tj-reg').click()

# 获得所有窗口
allhandles = driver.window_handles

# 循环判断窗口是否为当前窗口
for handle in allhandles:
    if handle != nowhandle:
        driver.switch_to_window(handle)
        print('Now register window ~~!')
        driver.implicitly_wait(6)
        driver.find_element_by_name('userName').send_keys("username")
        time.sleep(5)
        driver.close()

# 回到原先的窗口
driver.switch_to_window(nowhandle)

driver.find_element_by_name('kw1').send_keys(u"注册成功！")
time.sleep(3)
driver.quit()
print("Test Case Complete !")
