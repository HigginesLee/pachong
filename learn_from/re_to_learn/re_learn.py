#user HigginesLee
#date 2022-1-7
'''
正则表达式(re)
元字符{
.  匹配除了\n以外的任意字符
\w 匹配字母、数字或下划线
\s 匹配任意空白符
\d 匹配数字
\t 匹配制表符
\n 匹配换行符
^  匹配开头
$  匹配末尾
\W \D \S 对与\w \d \s 的反义
a|b a或者b
() 组
[...] 字符组
[^...] 与字符组相反
}
量词{
* 重复零次或更多次
+ 重复一次或更多此
? 重复一次或零次
{n} 重复n次

.*? 尽可能少的匹配
.* 贪婪匹配
}
'''
import re
#findall:匹配字符串中所有符合正则的内容
lst=re.findall(r"\d+","我的电话是10086，你的电话是10010")
#print(lst) 

#finditer:匹配的是字符串中所有的内容，返回的是迭代器，从迭代器中获取内容.group()
it=re.finditer(r"\d+","我的电话是10086，你的电话是10010")
for i in it:
    print(i.group())

#search:拿到数据就返回，返回的是match对象，那数据需要.group()
s=re.search(r"\d+","我的电话是10086，你的电话是10010")
print(s.group())

# match 从头匹配
# 预加载正则表达式
obj=re.compile(r"\d+")
ret=obj.finditer("我的电话是10086，你的电话是10010")
for j in ret:
    print(j.group())

#从正则中提取内容------------(?P<分组名字>正则)
s='''
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>

'''
obj=re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>",re.S)#re.S:让.能匹配换行符
result=obj.finditer(s)
for item in result:
    print(item.group('id'))