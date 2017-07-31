__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/31
"""
    Description:
        testadd.py
"""
from calculator import Count
import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("Test start")

    def tearDown(self):
        print("Test complete")

    def test_add1(self):
        j =Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j=Count(41,76)
        self.assertEqual(j.add(),117)

if __name__ == '__main__':
    unittest.main()



