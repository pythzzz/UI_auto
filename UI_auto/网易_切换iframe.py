from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

# driver.get('https://mail.qq.com/')
#
# frame = driver.find_element('xpath', '//*[@id="login_frame"]')
#
# driver.switch_to.frame(frame)
#
# # driver.find_element('id', 'uin_tips').clear()
# time.sleep(2)
# driver.find_element('xpath', '//*[@id="u"]').send_keys('123')
# time.sleep(2)


driver.get('https://mail.163.com/?msg=authfail#return')
# 定位到登录页的iframe
frame = driver.find_element('tag name', 'iframe')
# 切换到登录页的iframe
driver.switch_to.frame(frame)

# driver.find_element('id', 'uin_tips').clear()
time.sleep(2)
driver.find_element('name', 'email').send_keys('123')
time.sleep(2)

# 切换回top页
driver.switch_to.default_content()
# 如果只有两层frame，可以切换回上一层，效果等同于切换回top页.如果已经在top页，则不生效。
driver.switch_to.parent_frame()
# 点击首页的帮助按钮
driver.find_element('xpath', '/html/body/div[2]/div[2]/a[7]').click()
time.sleep(2)
