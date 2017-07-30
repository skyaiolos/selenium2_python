__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        login model
"""
from selenium import webdriver
class login():
    # 登陆
    def user_login(self,driver):
        user = driver.find_element_by_id("idInput")
        user.clear()
        user.send_keys("username")
        pwd = driver.find_element_by_id("pwInput")
        pwd.clear()
        pwd.send_keys("123456")
        driver.find_element_by_id("loginbtn").click()

    # 退出
    def user_logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()

