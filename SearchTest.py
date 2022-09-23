import time

from selenium import webdriver
from selenium.webdriver.common.by import By

for i in range(0,10):
    # 记录开始时间
    start=time.perf_counter()
    driver = webdriver.Chrome()
    driver.get("https://www.bilibili.com/")

    # 找到搜索框，输入搜索内容，回车进行搜索
    driver.find_element(By.XPATH,'//*[@id="nav-searchform"]/div[1]/input').send_keys('selenium\n')

    # 输出用时
    print(round(time.perf_counter()-start))
    time.sleep(3)
    driver.close()