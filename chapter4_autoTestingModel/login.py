__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/29
"""
    Description:
        #登录模块  - login.py
"""
from selenium import webdriver
def login():
    driver = webdriver.Chrome()
    driver.find_element_by_id("tbUserName").send_keys("username")
    driver.find_element_by_id("tbPassword").send_keys("456123")
    driver.find_element_by_id("btnLogin").click()

