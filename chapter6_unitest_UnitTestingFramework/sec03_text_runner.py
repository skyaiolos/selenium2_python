__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        对 sec03_widget.py 被测试类，下面通过 PyUnit 编写完整的单元测试用例：
"""

from sec03_widget import Widget
import unittest


# 执行测试的类

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))

    def Resize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))


# 测试

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase.testSize)
    suite.addTest(WidgetTestCase("Resize"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
