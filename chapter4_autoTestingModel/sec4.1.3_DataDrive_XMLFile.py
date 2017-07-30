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

from xml.dom import minidom

# open the XML file
dom = minidom.parse('user_info.xml')

# Get the document element
root = dom.documentElement

tagname = root.getElementsByTagName('component')

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

print('--------------------')
tagname = root.getElementsByTagName('browser')
print(tagname[0].tagName)

tagname = root.getElementsByTagName('login')
print(tagname[1].tagName)

tagname = root.getElementsByTagName('province')
print(tagname[2].tagName)
