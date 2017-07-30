__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/29
"""
    Description:
       .1.3 数据驱动
数据驱动应该是自动化的一个进步；从它的本意来讲，数据的改变（更新）驱动自动化的执行，从而
引起测试结果的改变。这显然是一个非常高级的概念和想法。其实，我们可直白的理解成参数化，输入数
据的不同从而引起输出结果的变化。 
"""

from selenium import webdriver
import time

vualues = ['selenium', 'webdriver', u'我爱Python']

# 执行循环

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

for search_word in vualues:
    driver.find_element_by_id('kw').clear()
    time.sleep(1)
    search_field = driver.find_element_by_id("kw")
    search_field.send_keys(search_word)
    search_btn = driver.find_element_by_id("su")
    search_btn.click()
    time.sleep(2)

    pic = "%s.png" % search_word
    print(pic)
    driver.get_screenshot_as_file("./" + pic)

driver.quit()
