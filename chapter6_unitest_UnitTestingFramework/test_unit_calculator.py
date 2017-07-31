__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        
"""
from calculator import Count
import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        print("Test {}start!".format(self.__class__().name()))

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def tearDown(self):
        print("Test Add Complete!")


class TestSub(unittest.TestCase):
    def setUp(self):
        print("Test sub start")

    def tearDown(self):
        print("test sub complete")

    def test_sub(self):
        j = Count(5, 4)
        self.assertEqual(j.sub(), 1)


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd.test_add)
    suite.addTest(TestSub.test_sub)

    # Run
    runner = unittest.TextTestRunner()
    runner.run(suite)
