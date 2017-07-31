__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        
"""

from sec03_auto import Widget
import unittest


# execute the Class of testing
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    # 测试 getSize()方法的测试用例
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))

    # 测试 resize()方法的测试用例
    def Resize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))

    def tearDown(self):
        self.widget = None


# 构造测试集

def suite():
    suite = unittest.TestSuite()
    # suite.addTest(WidgetTestCase('testSize'))
    # suite.addTest(WidgetTestCase('testResize'))
    suite.addTest(WidgetTestCase.Resize)
    suite.addTest(WidgetTestCase.testSize)

    return suite


def suite_make():
    return unittest.makeSuite(WidgetTestCase, 'test')


# 测试
if __name__ == '__main__':
    unittest.main('suite')
    # unittest.main(defaultTest='suite_make')

# Only run the test case "testSize"
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK

"""
用 import 语句引入 unittest 模块
1.  让所有执行测试的类都继承于 TestCase 类，可以将 TestCase 看成是对特定类进行测试的方法的
集合
2.  setUp()方法中进行测试前的初始化工作，tearDown()方法中执行测试后的清除工作。setUp()
和 tearDown()都是 TestCase 类中定义的方法
3.  在 testSize()中调用 assertEqual()方法，对 Widget 类中 getSize()方法的返回值和预期值
进行比较，确保两者是相等的，assertEqual()也是 TestCase 类中定义的方法。
4.  提供名为 suite()的全局方法，PyUnit 在执行测试的过程调用 suit()方法来确定有多少个测试用
例需要被执行，可以将 TestSuite 看成是包含所有测试用例的一个容器。
"""
