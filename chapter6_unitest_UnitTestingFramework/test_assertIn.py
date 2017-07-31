__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/31
"""
    Description:
        2. 断言第一个参数是否在第二个参数中。
            - assertIn(first,second,msg=None)
            - assertNotIn(first,second,msg=None)
            
        3. 断言第一个参数和第二个参数是否为同一个对象
            - assertIsNone(expr,msg=None)
            - assertIsNOtNone(expr,msg=None)
        4. 断言表达式是否为None对象
            - assertIsInstance(obj,cls,msg=None)
            - assertNotIsInstance(obj,cls,msg=None)
        
        
"""
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test complete")

    def test_case(self):
        a = 'hello'
        b = 'hello world'
        self.assertIn(a, b, msg="a is not in b")


if __name__ == '__main__':
    unittest.main()
