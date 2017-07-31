__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/31
"""
    Description:
        如果setUp() 和tearDown() 做同一件事情就可以放在一个类里面
        
"""
from calculator import Count

import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        print("Test starting  ~~")

    def tearDown(self):
        print("Test complete !")


class TestAdd(MyTest):
    def test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5, msg="add count is wrong ")

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)


class TestSub(MyTest):
    def test_sub1(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)


if __name__ == '__main__':
    unittest.TestCase()
