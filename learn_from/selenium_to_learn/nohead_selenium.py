from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
option=webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-logging'])
option.add_argument("--headless")
option.add_argument('--disable-gpu')
web=webdriver.Chrome(options=option)
resp=web.get('https://www.baidu.com')
print(web.page_source)
# web.get("https://ys.endata.cn/BoxOffice/Ranking")

# #定位到下拉列表
# sel_el=web.find_element(By.XPATH,'')
# #对元素进行包装，包装成下拉菜单
# sel=Select(sel_el)
# #然后浏览器调整选项
# for i in range(len(sel.options)):#i就是每一个下拉框的索引位置
#     sel.select_by_index(i)