__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/27
"""
    Description:
        通过自动化测试脚本调用upfile.exe 程序，实现上传
        https://www.autoitscript.com/site
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os, time

driver = webdriver.Chrome()

file_path = 'file:///' + os.path.abspath("upload_file.html")

driver.get(file_path)
# 点击打开上传宽口
# driver.find_element_by_css_selector('body > div > div > input[type="file"]').click()
file_btn = WebDriverWait(driver, 10).until(lambda btn: driver.find_element_by_name("file"))
file_btn.click()

# 调用upfile.exe 脚本，
os.system(r"./upfile.exe")

time.sleep(3)
driver.get_screenshot_as_file("./Upfile.png")

driver.quit()
