__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        3.1.2 设置浏览器宽，高。
"""
import unittest
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://m.mail.10086.cn")

print("设置浏览器宽480、高800显示")
driver.set_window_size(480, 800)
driver.quit()
