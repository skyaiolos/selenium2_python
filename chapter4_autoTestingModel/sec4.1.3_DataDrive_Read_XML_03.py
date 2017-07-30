__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/29
"""
    Description:
       read_xml.py
       
       获取标签的属性值

"""

from xml.dom import minidom

# open the XML file
dom = minidom.parse('user_info.xml')

# Get the document element
root = dom.documentElement

logins = root.getElementsByTagName('login')

username1 = logins[0].getAttribute("username")
print(username1)
password1 = logins[0].getAttribute("password")
print(password1)

username2 = logins[1].getAttribute("username")
print(username2)
password2 = logins[1].getAttribute("password")
print(password2)

# admin
# admain_123456
# guest
# guest_34456546