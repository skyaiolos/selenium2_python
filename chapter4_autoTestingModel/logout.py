__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/29
"""
    Description:
        #退出模块 - quit.py
"""
from selenium import webdriver
def logout():
    driver = webdriver.Chrome()
    driver.quit()

