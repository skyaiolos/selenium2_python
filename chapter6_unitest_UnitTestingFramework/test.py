__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        
"""

from calculator import Count


class TestAdd:
    def test_add(self):
        try:
            j = Count(2, 4)
            add = j.add()
            assert (add == 5), "Integer addition result error!"

        except AssertionError as e:
            print(e)

        else:
            print('Test pass!')


mytest = TestAdd()
mytest.test_add()
