__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        第四节、批量执行测试用例
通过对前面对 unittest 框架的学习我们了解到，可以在一个.py 文件里编写多个测试用例，然后执行
文件里的所有用例，这显然是一个不错的做法，我们可以将一些相关的用例放到一个文件里，unittest 支
持这么做，但假如我们成百上千的用例呢，放一.py 文件显然有些不太合理。
比较合理的做法是把相关的几条用例放到一个.py 文件里，把所有.py 文件放到一个文件夹下，然后通
过一个程序执行文件夹下面的所有用例。
图 5.x
如图 5.x 显然是一个比较理想的效果，下面来组织这样一个结构。
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url = "http://www.baidu.com"
        self.verificationError = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationError)

    # 百度搜索用例
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        search_field = driver.find_element_by_id("kw")
        search_field.clear()
        search_field.send_keys('selenium webdriver')
        search_btn = driver.find_element_by_id('su')
        search_btn.click()
        time.sleep(2)
        driver.close()

    # 百度设置用例
    def test_baidu_set(self):
        driver = self.driver
        driver.get(self.base_url + "/gaoji/preference.html")
        driver.implicitly_wait(20)

        # 设置每页搜索结果为 100 条
        ##Good -  m = driver.find_element_by_name('NR')
        m = driver.find_element_by_xpath("//select[@name='NR']")
        time.sleep(1)
        m.find_element_by_xpath('//option[@value="100"]').click()

        time.sleep(2)

        # 保存设置的信息
        # #Failed -- driver.find_element_by_xpath('//input[@value = "保存设置"').click()
        driver.find_element_by_css_selector("#gxszButton > input:nth-child(1)").click()
        time.sleep(2)
        driver.switch_to_alert().accept()


if __name__ == '__main__':
    unittest.main()
