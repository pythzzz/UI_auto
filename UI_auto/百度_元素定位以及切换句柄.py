from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# 初始化浏览器
driver = webdriver.Chrome()
# 登录百度
driver.get('https://www.baidu.com')
# 网页刷新
driver.refresh()
# 定位到输入框，并输入Python
driver.find_element('id', 'kw').send_keys('python')
time.sleep(1)
# 点击’百度一下‘按钮
driver.find_element('id', 'su').click()
time.sleep(2)
# 返回上一步
driver.back()

driver.find_element('xpath', '//*[@id="s-top-left"]/a[6]').click()
print(driver.current_url)
print(driver.current_window_handle)
# 查询所有句柄
handles = driver.window_handles
# 切换到最新句柄
driver.switch_to.window(handles[-1])

time.sleep(2)
# 输出当前URL，验证是否切换句柄成功
print(driver.current_url)

# 关闭当前页面
driver.close()

driver.switch_to.window(handles[0])
print(driver.current_url)

# 关闭浏览器
driver.quit()
