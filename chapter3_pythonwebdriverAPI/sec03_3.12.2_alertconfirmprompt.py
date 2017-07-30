__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/28
"""
    Description:
        第十二节 alert/confirm/prompt  处理
webdriver 中处理 JavaScript 所生成的 alert、confirm 以及 prompt 是很简单的。具体思路是使用
switch_to.alert()方法定位到 alert/confirm/prompt。然后使用 text/accept/dismiss/send_keys 按需进行操做。
? text 返回 alert/confirm/prompt 中的文字信息。
? accept 点击确认按钮。
? dismiss 点击取消按钮，如果有的话。
? send_keys 输入值，这个 alert\confirm 没有对话框就不能用了，不然会报错。
所给出的是百度设置页面，在设置完成后点击“保存设置”所弹的提示框。下面通过脚本来
处理这个弹窗。

    switch_to_alert()
用于获取网页上的警告信息。我们可以对警告信息做以下操作：
"""

from selenium import webdriver
import time, os
from selenium.webdriver.support.ui import WebDriverWait

dirver = webdriver.Chrome()
dirver.get("http://www.baidu.com/")

# 点击打开搜索设置
dirver.find_element_by_css_selector("a.pf:nth-child(8)").click()
dirver.find_element_by_css_selector(".setpref").click()
time.sleep(3)

# click save setting
dirver.find_element_by_css_selector(".prefpanelgo").click()
# dirver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
# save_setting = WebDriverWait(dirver, 10).until(lambda btn: dirver.find_element_by_css_selector(".prefpanelgo"))
# save_setting.click()
# dirver.get_screenshot_as_file("./alert.png")

# 获取网页上的警告信息
alert = dirver.switch_to_alert()
time.sleep(3)

# 得到文本信息并打印
print(alert.text)

# 接收警告信息
alert.accept()
time.sleep(3)
dirver.get_screenshot_as_file("./afterSetting.png")

# 取消对话框（如果有的话）
# alert.dismiss()

# #输入值（如果有的话）
# alert.send_keys(“xxx”)

dirver.quit()
