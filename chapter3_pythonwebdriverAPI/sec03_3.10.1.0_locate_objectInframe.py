__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/27
"""
    Description:
        第十节 定位 frame  中的对象
在 web 应用中经常会出现 frame 嵌套的应用，假设页面上有 A、B 两个 frame，其中 B 在 A 内，那么
定位 B 中的内容则需要先到 A，然后再到 B。
switch_to_frame 方法可以把当前定位的主体切换了 frame 里。怎么理解这句话呢？我们可以从 frame
的实质去理解。frame 中实际上是嵌入了另一个页面，而 webdriver 每次只能在一个页面识别，因此才需要
用 switch_to.frame 方法去获取 frame 中嵌入的页面，对那个页面里的元素进行定位。
下面的代码中 frame.html 里有个 id 为 f1 的 frame，而 f1 中又嵌入了 id 为 f2 的 frame，该 frame 加载
了百度的首页。
frame.html
driver.switch_to_frame("f2")
"""

if __name__ == '__main__':
    pass

