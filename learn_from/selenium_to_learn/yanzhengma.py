#验证码的验证方式：
#   1.图像识别；2.互联网上成熟的验证码破解工具
# 超级鹰
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from Chaojiying_Python.chaojiying import Chaojiying_Client
import time
opt=ChromeOptions()
opt.add_experimental_option('excludeSwitches',['enable-logging'])
web=Chrome(options=opt)
web.get('http://www.chaojiying.com/user/login/')
#先处理验证码
img=web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('HigginsLee', 'euqhG29E.HWtiAe', '	927717')	
dic=chaojiying.PostPic(img,1902)
verify_code=dic['pic_str']
#填入
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('HigginsLee')
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('euqhG29E.HWtiAe')
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
#登陆
time.sleep(5)
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()