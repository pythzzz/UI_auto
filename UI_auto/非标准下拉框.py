from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
# 实例化鼠标操作actionchains
actionchains = ActionChains(driver)
driver.get('https://www.baidu.com/')
driver.maximize_window()
driver.implicitly_wait(10)

# 定位百度右上角设置按钮
ele = driver.find_element('xpath', '//*[@id="s-usersetting-top"]')
# 移动鼠标到设置按钮
actionchains.move_to_element(ele).perform()
time.sleep(2)
# 点击设置按钮下的搜索设置按钮
driver.find_element('xpath', '//*[@id="s-user-setting-menu"]/div/a[1]/span').click()
time.sleep(2)
# 点击搜索设置中的高级搜索
driver.find_element('xpath', '//*[@id="wrapper"]/div[6]/div/div/ul/li[2]').click()
time.sleep(2)

# 点击时间下拉框（非标准下拉框，不是select组件）
driver.find_element('xpath', '//*[@id="adv-setting-gpc"]/div/div[1]').click()
# 获取时间下拉框中所有元素
ele2 = driver.find_elements('xpath', '//*[@id="adv-setting-gpc"]/div/div[2]/div[2]/p')
print(ele2)
# 点击时间下拉框中第三个元素
ele2[3].click()

# 遍历点击时间下拉框中所有元素
for i in range(len(ele2)):
    driver.find_element('xpath', '//*[@id="adv-setting-gpc"]/div/div[1]').click()
    ele2[i].click()
    time.sleep(1)

time.sleep(2)
driver.quit()

# set = driver.find_element('link test',"设置")
# ActionChains(driver).move_to_element(set).perform()
# driver.find_element('link test',"搜索设置").click()
# # 定位下拉框，选择其中的选项
# sel = driver.find_element('css selector',"select#nr")
# sel.find_element('css selector',"option[value='20']").click()
# # 退出
# time.sleep(2)
# driver.quit()


driver.quit()
