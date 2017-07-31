__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/31
"""
    Description:
      - assertTrue(expr, msg="")
      - assertFalse(expr,msg+"")
"""

from count import is_prime
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("Test start")

    def tearDown(self):
        print("Test complete")

    def test_case(self):
        self.assertTrue(is_prime(7), msg="Is not prime!")


if __name__ == '__main__':
    unittest.main()
