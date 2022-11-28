from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

driver=webdriver.Chrome()
# 实例化Alert
alert=Alert(driver)


driver.get('http://u.lrswl.com/?action=login')
driver.find_element('name','image').click()
time.sleep(2)
# 获取弹窗文本
print(alert.text)
# 点击弹窗中确定按钮
alert.accept()
time.sleep(2)
# 点击取消按钮
# alert.dismiss()
# 在弹窗中发送文本
# alert.send_keys('xxx')

driver.quit()