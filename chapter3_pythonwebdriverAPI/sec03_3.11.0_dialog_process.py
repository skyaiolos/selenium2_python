__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/27
"""
    Description:
        第十一节 对话框处理
页面上弹出的对话框是自动化测试经常会遇到的一个问题；很多情况下对话框是一个 iframe，如上一
节中介绍的例子，处理起来稍微有点麻烦；但现在很多前端框架的对话框是 div 形式的，这就让我们的处
理变得十分简单。
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os, time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(5)

# 点击登录链接 -
#  ----如果by Class , Id 定位不到空间， 就要用by_css_selector (**推荐使用，稳定）
# driver.find_element_by_css_selector("a.lb:nth-child(7)").click()
## driver.find_element_by_name("tj_login").click()
logon = WebDriverWait(driver, 10).until(lambda logon: driver.find_element_by_css_selector("a.lb:nth-child(7)"))
logon.click()

logon_page = WebDriverWait(driver, 10).until(lambda page: driver.find_element_by_class_name("tang-body"))
print("登陆界面是否加载完成: {}".format(logon_page.is_displayed()))

try:
    # 通过二次定位找到用户名输入框
    div = driver.find_element_by_class_name("tang-body").find_element_by_name("userName")
    pwd = driver.find_element_by_class_name("tang-body").find_element_by_name("password")
    # WebElement  接口常用方法 (size,text , get_attribute(name),is_displayed()
    print("attribute is: {};\nsize is: {};\ntext is: {};\nis_diplayed: {};" \
          .format(div.get_attribute('type'), div.size, div.text, div.is_displayed()))

    div.send_keys("username")
    pwd.send_keys("1234")
    # driver.find_element_by_name("password").send_keys("password")

    driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

    driver.get_screenshot_as_file("./baidu_logon.png")

except Exception as e:
    print(e)

finally:
    driver.quit()
print("\nTest Case is completed !")
