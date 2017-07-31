__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        
"""

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        number = input("Enter a number:")
        self.number = int(number)

    def test_case(self):
        self.assertEqual(self.number, 10, msg="Your input is wrong")

    def tearDown(self):
        print("Test Complete ")


if __name__ == '__main__':
    unittest.main()
