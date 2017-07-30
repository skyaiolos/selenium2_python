__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/29
"""
    Description:
       .1.3 数据驱动
    读取csv 文件首先要导入csv 模块， 通过reader() 读取CSV文件，然后通过for 循环
便利文件中的每一行数据。

user_info.csv
testing,123455@126.com,23,man
testing2,123455@127.com,24,woman
testing3,123455@128.com,25,woman

"""

import csv

csv_file = open('user_info.csv', 'r', encoding='utf-8')
data = csv.reader(csv_file)

for line in data:
    print("Mail: {}".format(line[1]))
