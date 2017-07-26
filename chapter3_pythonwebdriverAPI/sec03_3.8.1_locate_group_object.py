__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/26
"""
    Description:
        第八节 定位一组对象
webdriver 可以很方便的使用 find_element 方法来定位某个特定的对象，不过有时候我们却需要定位一
组对象，WebElement 接口同样提供了定位一组元素的方法 find_elements。
定位一组对象一般用于以下场景：
    1.  批量操作对象，比如将页面上所有的 checkbox 都勾上
    2.  先获取一组对象，再在这组对象中过滤出需要具体定位的一些对象。比如定位出页面上所有的
checkbox，然后选择最后一个。
"""
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
import os

driver = webdriver.Chrome()
file_path = 'file://' + os.path.abspath('checkbox.html')
driver.get(file_path)
# 选择页面上所有的 tag name 为 input 的元素
Checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in Checkboxes:
    checkbox.checked()
driver.quit()
print("complete !")

'''
os.path.abspath()
os 模块为 python 语言标准库中的 os 模块包含普遍的操作系统功能。主要用于操作本地目录文件。
path.abspath()方法用于获取当前路径下的文件。另外脚本中还使用到 for 循环，对 inputs 获取的一组元素
进行循环，在 python 语言中循环变量（input）可以不用事先声明直接使用。
find_elements_by_xx(‘xx’)
find_elements 用于获取一组元素。
'''
