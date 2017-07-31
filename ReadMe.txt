第五章 自动化测试用例设计
本章将简单探讨自动化测试用例的设计，笔者认为不管是手工测试，自动化测试，还是性能测试都是
以测试用例为前提的。那么测试用例是测试人员综合自己人经验从需求中挖掘和提炼而来。所以不管什么
类型的测试工作，我们都不能盲目开展。任何测试工作都应该以需求为基础，以测试用例为导向进行实施。
第一节、 手工测试 用 例与自动化测试用 例
手工测试用例是针对手工测试人员，自动化测试用例是针对自动化测试框架，前者是手工测试用例人
员应用手工方式进行用例解析，后者是应用脚本技术进行用例解析，两者最大的各自特点在于，前者具有
较好的异常处理能力，而且能够基于测试用例，制造各种不同的逻辑判断，而且人工测试步步跟踪，能够
细致的定位问题。而后者是完全按照测试用例的方式测试，而且异常处理能力不强，往往一个自动化测试
用例运行完毕后，报一堆错误，对于测试人员来定位错误是一个难点，这样往往发现的问题很少。
手工测试用例与自动化测试用例对比：
手工测试用例
? 较好的异常处理能力，能通过人为的逻辑判断校验当前步骤的功能实现正确与否。
? 人工执行用例具有一定的步骤跳跃性。
? 人工测试步步跟踪，能够细致的定位问题。
? 主要用来发现功能缺陷
自动化测试用例
? 执行对象是脚本，任何一个判断都需要编码定义。
? 用例步骤之间关联性强。
? 主要用来保证产品主体功能正确完整和让测试人员从繁琐重复的工作中解脱出来。
博客园---虫师
http://fnng.cnblogs.com 112
? 目前自动化测试阶段定位在冒烟测试和回归测试。
通过对比我们可以看到，手工测试用例与自动化测试用例之间是存在差异的。所以，直接拿手工测试
用例来直接转化成自动化测试脚本。
在此笔者需要强调：自动化测试替代不了手工测试，目的仅仅在于让测试人员从繁琐重复的机械式测
试过程解脱出来，把时间和精力突入到更有价值的地方，从而挖掘更多的产品缺陷。目前自动化测试更多
的时候是定位在冒烟测试和回归测试；冒烟测试执行的是主体功能点的用例。回归测试执行全部或部分的
测试用例。
怎么编写自动化测试用例，如何将自动化测试用例和手工测试用例相辅相成。
用例选型注意事项：
1、 不是所有的手工用例都要转为自动化测试用例。
2、 考虑到脚本开发的成本，不要选择流程太复杂的用例。如果有必要，可以考虑把流程拆分多个
用例来实现脚本。
3、 选择的用例最好可以构建成场景。例如一个功能模块，分 n 个用例，这 n 个用例使用同一个场
景。这样的好处在于方便构建关键字测试模型。
4、 选择的用例可以带有目的性，例如这部分用例是用例做冒烟测试，那部分是回归测试等，当然，
会存在重叠的关系。如果当前用例不能满足需求，那么唯有修改用例来适应脚本和需求。
5、 选取的用例可以是你认为是重复执行，很繁琐的部分，例如字段验证，提示信息验证这类。这
部分适用回归测试。
6、 选取的用例可以是主体流程，这部分适用冒烟测试。
7、 自动化测试也可以用来做配置检查，数据库检查。这些可能超越了手工用例，但是也算用例拓
展的一部分。项目负责人可以有选择地增加。
8、 如果平时在手工测试时，需要构造一些复杂数据，或重复一些简单机械式动作，告诉自动化脚
本，让他来帮你。或许你的效率因此又提高了。
博客园---虫师
http://fnng.cnblogs.com 113
第 二 节、 测试类型
测试静态内容
静态内容测试是最简单的测试,用于验证静态的、不变化的 UI 元素的存在性。例如:
•每个页面都有其预期的页面标题?这可以用来验证链接指向一个预期的页面。
•应用程序的主页包含一个应该在页面顶部的图片吗?
•网站的每一个页面是否都包含一个页脚区域来显示公司的联系方式,隐私政策,以及商标信息?
•每一页的标题文本都使用的<h1>标签吗?每个页面有正确的头部文本内吗?
您可能需要或也可能不需要对页面内容进行自动化测试。如果您的网页内容是不易受到影响手工对内
容进行测试就足够了。如果,例如您的应用文件的位置被移动,内容测试就非常有价值。
测试链接
Web 站点的一个常见错误为的失效的链接或链接指向无效页。链接测试涉及点各个链接和验证预期的
页面是否存在。如果静态链接不经常更改,手动测试就足够。但是,如果你的网页设计师经常改变链接,或者
文件不时被重定向,链接测试应该实现自动化。
功能测试
在您的应用程序中,需要测试应用的特定功能,需要一些类型的用户输入,并返回某种类型的结果。通常
一个功能测试将涉及多个页面,一个基于表单的输入页面,其中包含若干输入字段、提交“和”取消“操作,
以及一个或多个响应页面。用户输入可以通过文本输入域,复选框,下拉列表,或任何其他的浏览器所支持的
输入。
功能测试通常是需要自动化测试的最复杂的测试类型,但也通常是最重要的。典型的测试是登录,注册
网站账户,用户帐户操作,帐户设置变化,复杂的数据检索操作等等。功能测试通常对应着您的应用程序的描
述应用特性或设计的使用场景。
测试动态元素
博客园---虫师
http://fnng.cnblogs.com 114
通常一个网页元素都有一个唯一的标识符,用于唯一地定位该网页中的元素。通常情况下,唯一标识符
用 HTML 标记的’id’属性或’name’属性来实现。这些标识符可以是一个静态的,即不变的、字符串常
量。
它们也可以是动态生产值,在每个页面实例上都是变化的。例如,有些 Web 服务器可能在一个页面实例
上命名所显示的文件为 doc3861,并在其他页面实例上显示为 doc6148,这取决于用户在检索的‘文档’。验
证文件是否存在的测试脚本,可能无法找到不变的识别码来定位该文件。通常情况下,具有变化的标识符的
动态元素存在于基于用户操作的结果页面上,然而,显然这取决于 Web 应用程序。
下面是一个例子。
这是一个 HTML 标记的复选框, 其 ID (addForm:_ID74:_ID75:0:_ID79:0:checkBox) 是一个动态生成
的值。这个页面下次被打开时入框的 ID 将可能是一个不同的值。
Ajax  的测试
Ajax 是一种支持动态改变用户界面元素的技术。页面元素可以动态更改,但不需要浏览器重新载入页
面,如动画,RSS 源,其他实时数据更新等等。Ajax 有不计其数的更新网页上的元素的方法。但是了解 AJAX
的最简单的方式,可以这样想,在 Ajax 驱动的应用程序中,数据可以从应用服务器检索,然后显示在页面上,而
不需重新加载整个页面。只有一小部分的页面,或者只有元素本身被重新加载。
断言 assert  与验证 verify
什么时候使用断言命令,什么时候使用验证命令?这取决于你。差别在于在检查失败时,你想让测试程序
做什么。你想让测试终止,还是想继续而只简单地记录检查失败?
这需要权衡。如果您使用的断言,测试将在检查失败时停止,并不运行任何后续的检查。有时候,也许是
经常的,这是你想要的。如果测试失败,你会立刻知道测试没有通过。TestNG 和 JUnit 等测试引擎提供在开
发测试脚本时常用的插件,可以方便地标记那些测试为失败的测试。优点:你可以直截了当地看到检查是否
通过。缺点:当检查失败,后续的检查不会被执行,无法收集那些检查的结果状态。
相比之下,验证命令将不会终止测试。如果您的测试只使用验证,可以得到保证是—假设没有意外的异
常—测试会被执行完毕,而不管是否发现缺陷。缺点:你必须做更多的工作,以检查您的测试结果。也就是说,
你不会从 TestNG 和 JUnit 得到反馈。您将需要在打印输出控制台或日志文件中查看结果。每次运行测试,
你都需要花时间去查看结果输出。如果您运行的是数以百计的测试,每个都有它自己的日志，这将耗费时间。
及时得到反馈会更合适,因此断言通常比验证更常使用。
博客园---虫师
http://fnng.cnblogs.com 115
第 三 节、python  异常断言
在实际的脚本开发中，我们需要用到 python 的异常处理来捕捉异常和抛异常，所以我们有需要学习
和使用 python 的异常处理。
>>> open('abc.txt','r')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'abc.txt'
打开一个不存在的文件 abc.txt 文件，当系统找不到 abc.txt 文件时，就会抛出给我们一个 IOError 类
型的错误，No such file or directory：abc.txt （没有 abc.txt 这样的文件或目录）
Try...except...
假如，我们已经知道这种类型的错误，那么就可以通过一个异常扑捉来扑捉这个错误。我们可以通过
try... 来接收这个错误。打开文件写入：
try:
open("abc.txt",'r')
except IOError:
pass
再来运行程序就会看不到任何错误，因为我们用 except 接收了这个 IOError 错误。pass 表示实现了
相应的实现，但什么也不做。
假如我不是打开一个文件，而是输出一个没有定义的变量呢？
try:
print aa
except IOError:
pass
显然，在上面的代码中我并没有对 aa 赋值，运行结果：
博客园---虫师
http://fnng.cnblogs.com 116
Traceback (most recent call last):
File "/home/fnngj/py_se/tryy.py", line 3, in <module>
print aa
NameError: name 'aa' is not defined
我们已经用 except 接收错误了，为什么错误还是还是抛出来了。如果你细心会发现这一次的错误类
型是 NameError ，而我接收类型是 IOError ，所以要想接收这个 print 的错误，那么需要修改接收错误的
类型为 NameError
虽然，我知道 print 语句是可能会抛一个 NameError 类型的错误，虽然接收了这个类型错误，但我不
知道具体的错误提示信息是什么。那么，我能不能把错误信息打印出来呢？当然可以：
try:
print aa
except NameError, msg:
print msg
我们在接收错误类型的后面定义一个变量 msg 用于接收具体错误信息, 然后将 msg 接收的错误信息
打印。再来运行程序：
name 'aa' is not defined
现在只有一行具体错误信息。
异常的抛出机制：
1、如果在运行时发生异常，解释器会查找相应的处理语句（称为 handler）.
2、要是在当前函数里没有找到的话，它会将异常传递给上层的调用函数，看看那里能不能处理。
3、如果在最外层（全局“main”）还是没有找到的话，解释器就会退出，同时打印出 traceback 以便让用户
找到错误产生的原因。
注意：虽然大多数错误会导致异常，但一个异常不一定代表错误，有时候它们只是一个警告，有时候
它们可能是一个终止信号，比如退出循环等。
try...finally...
博客园---虫师
http://fnng.cnblogs.com 117
Try...finally...子句用来表达这样的情况：
我们不管线捕捉到的是什么错误，无论错误是不是发生，这些代码“必须”运行，比如文件关闭，释放
锁，把数据库连接返还给连接池等。
创建文件 poem.txt
图 5.1
tryf.py
import time
try:
f = file('poem.txt')
while True: # our usual file-reading idiom
line = f.readline()
if len(line) == 0:
break
time.sleep(2)
print line,
finally:
f.close()
print 'Cleaning up...closed the file'
运行程序(在 windows 命令提示符或 linux 终端下运行)：
...$ python tryf.py
abc
efg
^CCleaning up...closed the file
Traceback (most recent call last):
File "tryy.py", line 18, in <module>
time.sleep(2)
KeyboardInterrupt
程序读 poem.txt 文件中每一行数据打印，但是我有意在每打印一行之前用 time.sleep 方法暂停2秒钟。
这样做的原因是让程序运行得慢一些。在程序运行的时候，按 Ctrl-c 中断/取消程序。
博客园---虫师
http://fnng.cnblogs.com 118
我们可以观察到 KeyboardInterrupt 异常被触发，程序退出。但是在程序退出之前，finally 从句仍然被
执行，把文件关闭。
到目前为止，我们只讨论了如何捕捉异常，那么如何抛出异常呢？
Raise  抛出异常
使用 raise 来抛出一个异常：
tryr.py
#coding=utf-8
filename = raw_input('please input file name:')
if filename=='hello':
raise NameError('input file name error !')
程序要求用户输入一个文件名，如果用户输入的文件名是 hello ，那么抛出一个 NameError 的异常，
用户输入 hello 和 NameError 异常之间没有任何必然联系，我只是人为的通过 raise 来这样定义，我当然也
可以定义称 TypeError ，但我定义的异常类型必须是 python 提供的。
图 5.2
博客园---虫师
http://fnng.cnblogs.com 119
第 四 节、weddriver  错误截图
Webdriver 提供错误截图函数 get_screenshot_as_file()，可以帮助我们跟踪 bug，在脚本无法继续执行
时候， get_screenshot_as_file()函数将截取当前页面的截图保存到指定的位置，这是一个非常棒的功能，下
面实例展示 get_screenshot_as_file()函数的使用。
#coding=utf-8
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
#捕捉百度输入框异常
try:
browser.find_element_by_id("kwsss").send_keys("selenium")
browser.find_element_by_id("su").click()
except:
browser.get_screenshot_as_file("/home/fnngj/python/error_png.png")
browser.quit()
显然，我们对百度输入框的 id 定位动了手脚，并没有 id=kwsss 元素，所以脚本运行到此处后就无法
继续执行了，我们通过 try 对捕捉了这个异常，在 except 中，我们通过 get_screenshot_as_file()函数截图当
前页面并保存到指定的路径下面。
打开/home/fnngj/python/ 我们将看到生成的 error_png.png 文件：
博客园---虫师
http://fnng.cnblogs.com 120
图5.3
第 五 节、 自动化测试用 例 设计实例
上一节我们简单讨论了手工测试用例与自动化测试用之间的差异，以及自动化测试用例设计时的注意
事项，这一节就通过实例向读者介绍如何编写具体的自动化测试用。
笔者以快播私有云产品为例：
http://webcloud.kuaibo.com/
快播私有云是快播社区的产品之一，为用户提供免费的在线空间，读者进入空间后可以收藏用户分享
的影片，同时可以将自己的影片分享给其他用户。对于私有云本身具有创建文件夹，文件/文件夹重命名，
删除到回收，文件/文件夹的移动，去除重复影片，影片播放等功能。
在编写用例之间，笔者再次强调几点编写自动化测试用例的原则：
1、一个脚本是一个完整的场景，从用户登陆操作到用户退出系统关闭浏览器。
2、一个脚本脚本只验证一个功能点，不要试图用户登陆系统后把所有的功能都进行验证再退出系统
博客园---虫师
http://fnng.cnblogs.com 121
3、尽量只做功能中正向逻辑的验证，不要考虑太多逆向逻辑的验证，逆向逻辑的情况很多（例如手
号输错有很多种情况），验证一方面比较复杂，需要编写大量的脚本，另一方面自动化脚本本身比较脆弱，
很多非正常的逻辑的验证能力不强。（我们尽量遵循用户正常使用原则编写脚本即可）
4、脚本之间不要产生关联性，也就是说编写的每一个脚本都是独立的，不能依赖或影响其他脚本。
5、如果对数据进行了修改，需要对数据进行还原。
6、在整个脚本中只对验证点进行验证，不要对整个脚本每一步都做验证。
5.5.1 登陆用例实例
图5.4
笔者建议通过 excle 表格来编写自动化测试用例。
用例001：
用例 id login 用户登录
步骤： 动作 数据 验证点
1 打开打开登陆页 http://webcloud.kuaibo.com
2 用户登陆 username 123456 匹配用户昵称“虫师”
3 用户退出
备注：通过匹配用户登录之后的昵称来判断用户是否登录成功。
用例脚本（login.py）：
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
博客园---虫师
http://fnng.cnblogs.com 122
driver = webdriver.Firefox()
driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fwebcloud
.kuaibo.com%2F")
driver.maximize_window() #浏览器最大化
#登陆快播私有云
driver.find_element_by_id("user_name").send_keys("testing360")
driver.find_element_by_id("user_pwd").send_keys("198876")
driver.find_element_by_id("dl_an_submit").click()
time.sleep(3)
#获取用户名
now_user=driver.find_element_by_xpath("//div[@id='Nav']/ul/li[4]/a[1]/span")
.text
#用户名是否等于虫师，不等于将抛出异常
if now_user==u'虫师':
print '登陆成功'
else:
raise NameError('user name error!')
#退出
driver.find_element_by_class_name("Usertool").click()
time.sleep(2)
driver.find_element_by_link_text("退出").click()
time.sleep(2)
driver.close()
博客园---虫师
http://fnng.cnblogs.com 123
5.5.2 添加文件用例实例
图5.5
用例002：
用例 id collect 添加用户分享文件
步骤： 动作 数据 验证点
1 打开打开登陆页 http://webcloud.kuaibo.com
2 用户登陆 username 123456
3 收藏用户分享文件 判断列表文件总数加1
4 用户退出
备注：通过计算用户列表中的文件的数量来判断文件是否添加成功。
用例脚本（collect.py）：
注：用例登陆与退出参考用例001，本用例只关注收藏用户分享的逻辑代码。
#判断当前文件个数
inputs=driver.find_elements_by_tag_name('input')
n=0
for i in inputs:
if i.get_attribute('type')=="checkbox":
n=n+1
print u"当前列表文件为 %d" %n
博客园---虫师
http://fnng.cnblogs.com 124
#收藏用户分享文件
driver.find_element_by_class_name("collect").click()
time.sleep(3)
#再次获取当前文件的个数
inputs=driver.find_elements_by_tag_name('input')
ns=0
for ii in inputs:
if ii.get_attribute('type')=="checkbox":
ns=ns+1
print u"当前列表文件为 %d" %ns
#判断执行收藏文件之后比收藏之间文件加1 ，否则抛异常
f ns==n+1:
print "ok!"
else:
raise NameError('添加文件失败!！')
博客园---虫师
http://fnng.cnblogs.com 125
5.5.3 删除文件用例实例
图5.6
用例003：
用例 id del_one_file 删除单个文件
步骤： 动作 数据 验证点
1 打开打开登陆页 http://webcloud.kuaibo.com
2 用户登陆 username 123456
3 删除单个文件 判断列表文件总数减1
4 添加文件1个文件
5 用户退出
备注：因为删除了一个文件对文件的数据发生的改变，如果多次执行脚本，列表中的文件被删除完了
就会引，所以在删除一个文件后，需要再添加一文件，但添加文件操作不做验证。
用例脚本（del_one_file.py）：
#判断当前文件个数
inputs=driver.find_elements_by_tag_name('input')
n=0
for i in inputs:
if i.get_attribute('type')=="checkbox":
n=n+1
print u"当前列表文件为 %d" %n
博客园---虫师
http://fnng.cnblogs.com 126
#删除操作
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[4]/table/
tbody/tr/td/input").click()
driver.find_element_by_class_name("dele").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div").click()
time.sleep(4)
#再次获取当前文件的个数
inputs=driver.find_elements_by_tag_name('input')
ns=0
for ii in inputs:
if ii.get_attribute('type')=="checkbox":
ns=ns+1
print u"当前列表文件为 %d" %ns
#判断执行删除单个文件之后比删除之后文件减1 ，否则抛异常
f ns==n-1:
print "ok!"
else:
raise NameError('删除文件失败!！')
#收藏用户分享单个文件
driver.find_element_by_class_name("collect").click()
time.sleep(3)
博客园---虫师
http://fnng.cnblogs.com 127
5.5.4 重命名文件用例实例
图5.7
用例004：
用例 id renaming 文件重命名
步骤： 动作 数据 验证点
1 打开打开登陆页 http://webcloud.kuaibo.com
2 用户登陆 username 123456
3 文件重命名 新文件名
4 用户退出
备注：文件的重命名其实我们很难找到证据（验证点）证明重命名成功，那么脚本整个运行没有报错，
我们也可模糊的判断功能测试是 OK 的。
用例脚本（renaming.py）
#勾选重命名的文件
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[4]/table/
tbody[5]/tr/td/input").click()
time.sleep(3)
#鼠标移动到“更多”按钮弹下拉框
博客园---虫师
http://fnng.cnblogs.com 128
element=driver.find_element_by_class_name("more-fe")
ActionChains(driver).move_to_element(element).perform()
time.sleep(2)
#在 li 标签（更多 下拉框）中筛选到 data-action==rename（重命名）选项点击
lis=driver.find_elements_by_tag_name('li')
for li in lis:
if li.get_attribute('data-action') == 'rename':
li.click()
time.sleep(2)
在 input 标签中筛选 type==text 的重命名输入框
inputs=driver.find_elements_by_tag_name('input')
for input in inputs:
if input.get_attribute('type') == 'text':
input.send_keys(u"新文件名") #进行重名操作
input.send_keys(Keys.ENTER) #回车确认重命名
time.sleep(2)
总结：
在本章中，简单对比了手工测试用户与自动化测试用例的区别，自动化测试用例编写的原则，如何通
过 python 捕捉异常和抛出异常，以及 webdriver 提供的 get_screenshot_as_file()函数，以及如何编写
自动化用例与脚本等。
不过笔者先不要急于开始实施自动化测试，虽然我们可以编写单个的测试用例，并通过异常捕捉判断
用例是否运行成功。但只有与通过测试框架的整合，我们才能真正有效可行的运用自动化测试技术。