__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        1.  Test Case
        2.  Test Suit
        3.  Test Runner
        4   Test Fixture
"""

from calculator import Count
import unittest


class TestCount(unittest.TestCase):
    def setUp(self):
        print("Test start")

    def test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

    def tearDown(self):
        print("Test Complete!")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
