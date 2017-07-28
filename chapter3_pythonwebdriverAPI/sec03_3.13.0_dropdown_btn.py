__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/28
"""
    Description:
       第十三节 下拉框处理
下拉框也是 web 页面上非常常见的功能，webdriver 对于一般的下拉框处理起来也相当简单，要想定
位下拉框中的内容，首先需要定位到下拉框；这样的二次定位，我们在前面的例子中已经有过使用，下面
通过一个具体的例子来说明具体定位方法。 
"""
from selenium import webdriver
import time, os

driver = webdriver.Chrome()

file_path = 'file:///' + os.path.abspath("drop_down.html")

driver.get(file_path)

driver.implicitly_wait(3)

m = driver.find_element_by_id("ShippingMethod")
time.sleep(2)

# GOOD - by_xpath('//option[@value="10.69"]')
# m.find_element_by_xpath('//option[@value="10.69"]').click()

# GOOD - by_css_selector('#ShippingMethod > option[value="10.69"]')
m.find_element_by_css_selector('#ShippingMethod > option[value="10.69"]').click()
time.sleep(3)

print(m.find_element_by_xpath('//option[@value="10.69"]').text)
# print(m.find_element_by_css_selector("#ShippingMethod > option[value='10.69']").text)

# ShippingMethod > option:nth-child(3)

driver.quit()
