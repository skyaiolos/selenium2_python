__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/30
"""
    Description:
        __init__()
__init__()方法在类的一个对象被建立时，马上运行。这个方法可以用来对你的对象做一些你希望的初
始化。
getSize()
在面向对象的编程语言中都会有类的概念，类具有封装性；在 C++ 、java 等语言中通过 private（私
有）、protected（保护）、public（公有）等修饰符来限定访问权限。在 Python 中没有显式的 private 和 public
限定符，如果要将一个方法声明为 private 的，只要在方法名前面加上“ __ ”即可。
所以，我们前面定义的__init__() 方法是一个私有的方法，不能直接被外部使用。那么如何才能使用
类中私有的成员函数着，就通过 getXX 和 setXX 方法来访问。一个赋值函数（getXX），一个取值函数
(setXX )。
从上面的例子中看到，__init__()方法中默认参数是 size=(40, 40) 在函数体中定义 self._size = size。通
过变量传递，self._size=(40, 40) ，但 self._size 是私有的，不可被类以外的方法和函数调用。（self 表示类
本身，后面章节中会进一步解释。）
所以，在 getSize()方法中定义返回 self._size，那么就可以调用 getSize()方法来使用__init__()方法中
self._size。
"""


class Widget:
    def __init__(self, size=(40, 40)):
        self._size = size

    def getSize(self):
        return self._size

    def resize(self, width, height):
        if width < 0 or height < 0:
            raise (ValueError, "illegal size")
        self._size = (width, height)

    def dispose(self):
        pass
