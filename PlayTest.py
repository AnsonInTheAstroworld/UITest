import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import Cookies

# 获取cookies，以绕过测试中的登录
url = "https://www.bilibili.com/"
cookies = Cookies.getCookies(url)

for i in range(0,10):
    # 记录开始时间
    start=time.perf_counter()

    # 不登陆页面中不一定存在recommended-card
    driver=webdriver.Chrome()
    driver.get("https://www.bilibili.com/")
    Cookies.addCookies(driver,cookies)
    driver.find_element(By.CLASS_NAME, 'recommended-card').click()

    print(round(time.perf_counter()-start))
    time.sleep(3)
    driver.close()