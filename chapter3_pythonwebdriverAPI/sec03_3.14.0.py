__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/28
"""
    Description:
        第十四节 分页处理
对于 web 页面上的分页功能，我们一般做做以下操作：
? 获取总页数
? 翻页操作（上一页，下一页）
对于有些分页功能提供上一页，下一页按钮，以及可以输入具体页面数跳转功能不在本例的讨论范围
"""

from selenium import webdriver
import time, os

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

# 将页面滚动条拖到底部
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)

# 将滚动条移动到页面的顶部
js_ = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js_)
time.sleep(3)
