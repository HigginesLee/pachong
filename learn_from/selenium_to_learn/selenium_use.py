#selenium的各种操作
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
option=webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-logging'])
web=webdriver.Chrome(options=option)
# web.get("https://www.lagou.com")

#找到某个元素，，点击它
'''
原始的，现在已弃用
el=web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
'''
# el=web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a')

# el.click()#点击事件
# time.sleep(1) #让浏览器缓一下
# #找到输入框，输入python==>回车或点击搜索按钮
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER)
# time.sleep(2)
# #查找信息
# # lst=web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')
# # for li in lst:
# #     job_name=li.find_element(By.TAG_NAME,'a').text
# #     price=li.find_element(By.XPATH,'./div/div/div[2]/span').text
# #     com_name=li.find_element(By.XPATH,'./div/div[2]/div/a').text
# #     print(job_name,com_name,price)

# web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[2]/div[1]/div[1]/div[1]/a').click()
# #如何进入新窗口
# #切换新窗口
# web.switch_to.window(web.window_handles[-1])#切换到最后一个窗口
# #在新窗口中提取内容
# sl=web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]').text
# print(sl)
# web.close()
# web.switch_to.window(web.window_handles[0])
# print(web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[2]/div[1]/div[1]/div[1]/a').text)

#如果界面中遇到了iframe如何处理
#处理iframe，先拿到iframe，切换视角到iframe,然后在拿到数据
web.get('https://www.ttjj.cc/play/705-1-0.html')
time.sleep(3)
iframe=web.find_element(By.XPATH,'//*[@id="cciframe"]')
web.switch_to.frame(iframe)
iframe2=web.find_element(By.XPATH,'//*[@id="player"]/iframe')
web.switch_to.frame(iframe2)
t3=web.find_element(By.XPATH,'/html/body/script[@src]').text
print(t3)
web.switch_to_default_content()#切换回源界面