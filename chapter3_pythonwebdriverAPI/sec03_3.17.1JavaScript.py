__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/28
"""
    Description:
        第十七节 调用 JavaScript
当 webdriver 遇到没法完成的操作时，笔者可以考虑借用 JavaScript 来完成，比下下面的例子，
通过 JavaScript 来隐藏页面上的元素。除了完成 webdriver 无法完成的操作，如果你熟悉 JavaScript
的话，那么使用 webdriver 执行 JavaScript 是一件非常高效的事情。
webdriver 提供了 execute_script() 接口用来调用 js 代码。
执行 js 一般有两种场景：
1.  一种是在页面上直接执行 JS
2.  另一种是在某个已经定位的元素上执行 JS
execute_script(script, *args)
在当前窗口/框架 同步执行 javaScript
script：JavaScript 的执行。
*args：适用任何 JavaScript 脚本。
关于JavaScript代码的解析不在本书的范围之内，请读者通过其它资料学习理解JavaScript的使用。
"""

from selenium import webdriver
import time, os

driver = webdriver.Chrome()

file_path = 'file:///' + os.path.abspath('js.html')

driver.get(file_path)

#######通过 JS 隐藏选中的元素##########第一种方法：
# 隐藏文字信息
driver.execute_script('$("#tooltip").fadeOut();')

time.sleep(5)

# 隐藏按钮：
btn = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()', btn)
time.sleep(5)
driver.get_screenshot_as_file("./fadeout.png")
driver.quit()
