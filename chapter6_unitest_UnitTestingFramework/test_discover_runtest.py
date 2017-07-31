__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/31
"""
    Description:
        runtest.py
"""
import unittest

import test_discover_testadd, test_discover_testsub

suite = unittest.TestSuite()
suite.addTest(test_discover_testadd.TestAdd("test_add1"))
suite.addTest(test_discover_testadd.TestAdd("test_add2"))

suite.addTest(test_discover_testsub.Testsub("test_sub1"))
suite.addTest(test_discover_testsub.Testsub("test_sub2"))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
