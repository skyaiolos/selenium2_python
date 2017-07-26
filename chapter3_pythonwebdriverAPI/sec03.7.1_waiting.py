__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/26
"""
    Description:
        第七节 设置等待时间
有时候为了保证脚本运行的稳定性，需要脚本中添加等待时间。
sleep()：设置固定休眠时间。python 的 time 包提供了休眠方法 sleep() ，导入 time包后就可以使用 sleep()
进行脚本的执行过程进行休眠。
implicitly_wait()：是 webdirver 提供的一个超时等待。隐的等待一个元素被发现，或一个命令完成。
如果超出了设置时间的则抛出异常。
WebDriverWait()：同样也是 webdirver 提供的方法。在设置时间内，默认每隔一段时间检测一次当前
页面元素是否存在，如果超过设置时间检测不到则抛出异常。
下面通过实例来展示方法的具体使用：
"""

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("kw"))
element.send_keys("selenium")
driver.implicitly_wait(30)
driver.find_element_by_id('su').click()
time.sleep(5)
driver.quit()
print("the case is complete!")

"""
implicitly_wait()
implicitly_wait()方法比 sleep() 更加智能，后者只能选择一个固定的时间的等待，前者可以在一个时间
范围内智能的等待。
WebDriverWait()
详细格式如下：
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver - WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
timeout - 最长超时时间，默认以秒为单位
poll_frequency - 休眠时间的间隔（步长）时间，默认为 0.5 秒
ignored_exceptions - 超时后的异常信息，默认情况下抛 NoSuchElementException 异常。

实例：
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(“someId”))
is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).
until_not(lambda x: x.find_element_by_id(“someId”).is_displayed())

WebDriverWai()一般由 unit()或 until_not()方法配合使用，下面是 unit()和 until_not()方法的说明。
until(method, message=’’)
调用该方法提供的驱动程序作为一个参数，直到返回值不为 False。

until_not(method, message=’’)
调用该方法提供的驱动程序作为一个参数，直到返回值为 False。

"""
