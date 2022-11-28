from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/dragDropDataTransfer.htm')
driver.maximize_window()
driver.implicitly_wait(10)
action = ActionChains(driver)

driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
# 定位需要拖动的元素
source = driver.find_element('xpath','//*[@id="dragger"]')
# 需要拖动到的位置
target = driver.find_element('xpath','/html/body/div[5]')

time.sleep(2)
# 通过drag_and_drop方法模拟鼠标拖动操作
action.drag_and_drop(source, target).perform()

time.sleep(2)
driver.quit()
