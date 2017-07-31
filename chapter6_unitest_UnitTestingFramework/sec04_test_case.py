__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        下面编写 test_case.py 点文件来读取 test_case 文件夹下的文件：
        python 的 os 模块可以用来操作本地文件，通过 os.listdir()函数获得指定目录中的内容；下面通过
小例子单独理解这段程序的匹配用法。打开 python IDLE 的交互模式输入以下代码
"""

import os

# 列出某个文件夹下的所有 case,这里用的是 python，
# 所在 py 文件运行一次后会生成一个 pyc 的副本
caselist = os.listdir(r"./test_case")

for case in caselist:
    print(case)
    s = case.split('.')[1]
    print(s)
    if s == "py":
        # 此处执行 dos 命令并将结果保存到 log.txt
        os.system(
            r'G:\GitHub_Repository\selenium2_python\chapter6_unitest_UnitTestingFramework\test_case\%s 1>>log.txt 2>&1' % case)
