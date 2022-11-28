from selenium import webdriver
import time
import json

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

# 获取浏览器名称
print(driver.name)

# 获取当前网页标题
print(driver.title)

# 获取配置信息
abc = driver.capabilities
with open('./配置.json', 'w', encoding='utf-8') as ff:
    # 字典转换成json，并格式化
    json.dump(abc, ff, sort_keys=True, indent=4, separators=(",", ":"))

# 获取网页源码
# print(driver.page_source)
# 将网页源码写入一个文件
with open('./source.html', 'w', encoding='utf-8') as f:
    source = driver.page_source
    f.write(source)

driver.quit()