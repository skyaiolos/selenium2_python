__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/27
"""
    Description:
        通过对上面代码的分析，发现两个下拉菜单中每个选项的 link text 都相同，href 也一样，所以在这
里就需要使用层级定位了。
具体思路是：先点击显示出 1 个下拉菜单，然后再定位到该下拉菜单所在的 ul，再定位这个 ul 下的
某个具体的 link 。在这里，我们定位第 1 个下拉菜单中的 Another action 这个选项。
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os, time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('level_locate.html')
driver.get(file_path)
# 点击 Link1 链接（弹出下拉列表）
driver.find_element_by_link_text('Link1').click()

# 在父亲元件下找到 link 为 Action 的子元素
menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Another action')

# 鼠标移动到子元素上
ActionChains(driver).move_to_element(menu).perform()
time.sleep(4)
driver.get_screenshot_as_file("./第九层级定位——1.png")

driver.quit()
"""
driver.find_element_by_id('xx').find_element_by_link_text('xx').click()
这里用到了二次定位，通过对 Link1 的单击之后，出现下拉菜单，先定位到下拉菜单，再定位下拉菜
单中的选项。当然，如果菜单选项需要单击，可通过二次定位后也直接跟 click()操作。
ActionChains(driver)
driver: wedriver 实例执行用户操作。
ActionChains 用于生成用户的行为；所有的行为都存储在 actionchains 对象。通过 perform()执行存储的
行为。
move_to_element(menu)
move_to_element 方法模式鼠标移动到一个元素上，上面的例子中 menu 已经定义了他所指向的是哪一
个元素。
perform()
执行所有 ActionChains 中存储的行为。
"""