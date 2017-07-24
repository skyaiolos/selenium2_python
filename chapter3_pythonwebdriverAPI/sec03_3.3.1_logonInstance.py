__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/24
"""
    Description:
        下面以百度云登录实例来展示常见元素操作的使用：  
            

"""
from selenium import webdriver
import os, time

try:
    if not os.path.exists("./Captures"):
        os.mkdir("./Captures")
except OSError:
    pass
driver = webdriver.Chrome()
driver.get("http://yun.baidu.com/")
driver.maximize_window()
driver.get_screenshot_as_file("./Captures/baiduyun_default.png")
# by_XPath
# driver.find_element_by_xpath("//*[@id='login-middle']/div/div[6]/div[2]/a").click()

# by_class
driver.find_element_by_class_name("account-title").click()

driver.get_screenshot_as_file("./Captures/logon_page.png")

input_name = "TANGRAM__PSP_4__userName"
driver.find_element_by_id("TANGRAM__PSP_4__userName").clear()
driver.find_element_by_id(input_name).send_keys("jinsky0426")
input_pwd = "TANGRAM__PSP_4__password"
driver.find_element_by_id("TANGRAM__PSP_4__password").clear()
driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("234")

driver.get_screenshot_as_file("./Captures/UserLogon.png ")

driver.find_element_by_id("TANGRAM__PSP_4__submit").submit()

time.sleep(3)
driver.get_screenshot_as_file("./Captures/Logon.png")
if __name__ == '__main__':
    pass
