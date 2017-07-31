__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/31
"""
    Description:
        用于判断质数
"""

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2,n):
        if n % i ==0:
            return False
    return True



