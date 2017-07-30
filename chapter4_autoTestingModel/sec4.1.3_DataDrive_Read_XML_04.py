__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/29
"""
    Description:
       read_xml.py
        获得标签对之间的数据


"""

from xml.dom import minidom

# open the XML file
dom = minidom.parse('user_info.xml')

# Get the document element
root = dom.documentElement

privences = root.getElementsByTagName('province')
citys = root.getElementsByTagName('city')

# Get the second 'province' tag's value.
p2 = privences[1].firstChild.data
print(p2)

# Get the value of the first for the City
c1 = citys[0].firstChild.data
print('\t-' + c1)

# Get the second city
c2 = citys[1].firstChild.data
print('\t-' + c2)
#
# 广东
# 	-深圳
# 	-珠海
