# coding=utf-8
__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        
"""
from selenium import webdriver

driver = webdriver.Chrome()
base_utl ="https://openapi.baidu.com/oauth/2.0/authorize?client_id=wiE55BGOG8BkGnpPs6UNtPbb&response_type=code&redirect_uri=http%3A%2F%2Fnaotu.baidu.com%2Fuser%2Flogin_cb&scope=&state=5359b36514812454627763b1d3a57df8&display=popup"
driver.get(base_utl)
driver.find_element_by_id()
if __name__ == '__main__':
    pass

