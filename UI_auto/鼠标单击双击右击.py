from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/clicks.htm')
driver.maximize_window()
driver.implicitly_wait(10)
# 用浏览器驱动实例化鼠标操作的类
action = ActionChains(driver)

# 点位需要双击的元素
ele1 = driver.find_element('xpath', '/html/body/form/input[2]')
action.double_click(ele1).perform()
time.sleep(2)

# 定位需要单击的元素
ele2 = driver.find_element('xpath', '/html/body/form/input[3]')
action.click(ele2).perform()
time.sleep(1)
driver.find_element('xpath', '/html/body/form/input[3]').click()
time.sleep(2)

# 定位需要右击的元素
ele3 = driver.find_element('xpath', '/html/body/form/input[4]')
action.context_click(ele3).perform()
time.sleep(2)

# 判断按钮是否可用
a = driver.find_element('xpath', '/html/body/form/input[5]').is_enabled()
print(a)
time.sleep(2)
driver.close()
# time.sleep(2)
