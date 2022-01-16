#能否让程序连接到浏览器，让浏览器完成各种复杂的操作，我们只接受最终的结果
#selenium:自动化测试工具
#可以:打开浏览器，可以像人一样操作
#程序员可以从selenium中可以直接提取各种信息
#环境搭建 
#   pip install selenium
#   浏览器驱动

#让selenium启动浏览器
from selenium .webdriver import Chrome
#1.创建浏览器
web=Chrome()
web.get("https://www.baidu.com")
print(web.title)