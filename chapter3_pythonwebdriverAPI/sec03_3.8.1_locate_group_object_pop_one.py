__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/26
"""
    Description:
        第八节 定位一组对象
下面通过 css 方式来勾选一组元素，打印当所勾选元素的个数并对最后一个勾选的元素取消勾选
"""
from selenium import webdriver
import os, time

driver = webdriver.Chrome()
file_path = 'file://' + os.path.abspath('checkbox.html')
driver.get(file_path)
# 选择页面上所有的 tag name 为 input 的元素
Checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in Checkboxes:
    checkbox.click()
time.sleep(3)
# 打印当前页面上 type 为 checkbox 的个数
print(len(driver.find_elements_by_css_selector('input[type=checkbox]')))

# 把页面上最后1个 checkbox 的勾给去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()

driver.get_screenshot_as_file("./Checkbox_group_pop.png")
driver.quit()
print("complete !")

'''
len()
len 为 python 语言中的方法，用于返回一个对象的长度（或个数）。
pop()
pop 也为 python 语言中提供的方法，用于删除指定们位置的元素，pop()为空默认选择最一个元素。
'''
