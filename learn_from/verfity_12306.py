
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
opt=ChromeOptions()
opt.add_experimental_option('excludeSwitches',['enable-logging'])
opt.add_argument('--disable-blink-features=AutomationControlled')
web=Chrome(options=opt)
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)
# js='return window.navigator.webdriver'
# print(web.execute_script(js))
web.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys('15688981517')
web.find_element(By.XPATH,'//*[@id="J-password"]').send_keys('bcoaod19990424ci')
login=web.find_element(By.XPATH,'//*[@id="J-login"]').click()
time.sleep(4)
btn=web.find_element(By.XPATH,'//*[@id="nc_1__scale_text"]/span')
webdriver.ActionChains(web).drag_and_drop_by_offset(btn,330,0).perform()
time.sleep(2)
# while True:
#     try:
#         action = webdriver.ActionChains(web)  # 利用行为链，持续按住并拖拽
#         span = web.find_element(By.XPATH,'//*[@id="modal"]')  # 获取滑块
#         action.drag_and_drop_by_offset(span, 330, 0).perform()  # 按住并拖动 >300px即可，选用330绰绰有余
#         # action.click_and_hold(span).perform()
#         # action.move_by_offset(xoffset=300,yoffset=0).perform() 另一张拖动
#         action.release()  # 释放
#         # print(web.execute_script(js))
#         time.sleep(2)
#         a = web.find_element_by_xpath('//*[@id="nc_1_refresh1"]')  # 查找刷新按钮，如果没有说明登录成功，执行except跳出循环
#         a.click()  # 如果刚刚滑动失败，则点击刷新，重新滑动
#         time.sleep(5)
#     except Exception as e:
#         print(e)
#         break
