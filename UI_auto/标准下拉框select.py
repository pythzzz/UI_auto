from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
# 本地写一个html文件，双击浏览器打开后复制浏览器地址
driver.get('file:///D:/project/UI_auto/%E6%A0%87%E5%87%86%E4%B8%8B%E6%8B%89%E6%A1%86.html')
time.sleep(2)

# 定位下拉框元素
ele = driver.find_element('id', 'test')
# 用下拉框元素实例化Select
select = Select(ele)
# 通过索引获取下拉框元素
select.select_by_index(0)
time.sleep(2)
# 通过元素的值来获取
select.select_by_value('qy')
time.sleep(2)
# 通过元素的文本来获取
select.select_by_visible_text('春花')
time.sleep(2)

# 通过options遍历下拉框元素
for i in select.options:
    print(i.text)
    i.get_attribute('value')
    i.click()
    time.sleep(1)

driver.quit()
