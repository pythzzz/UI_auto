from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
time.sleep(2)
# 使用绝对路径（需要使用反斜\），但是在项目中会报错，别人找不到你电脑中的文件，所以建议使用os模块
driver.find_element('xpath', '//*[@id="file"]').send_keys('C:/Users/admin/Desktop/高并发.jmx')
time.sleep(2)

# 使用os模块获取路径，os.getcwdu()或者os.path.dirname(__file__)
mypath = os.getcwd()
# mypath=os.path.dirname(__file__)
print(mypath)
realpath = os.path.join(mypath, '标准下拉框.html')
driver.find_element('xpath', '//*[@id="file5"]').send_keys(realpath)
time.sleep(2)
