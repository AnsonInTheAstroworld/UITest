import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import Cookies

# 获取cookies，以绕过测试中的登录
url = "https://www.bilibili.com/"
cookies = Cookies.getCookies(url)

for i in range(0, 10):
    # 记录开始时间
    start=time.perf_counter()

    driver = webdriver.Chrome()
    driver.get(url)

    # 加入cookies，绕过登录
    Cookies.addCookies(driver, cookies)

    # 找到第一个推荐视频并点击
    driver.find_element(By.CLASS_NAME, 'recommended-card').click()

    # 转到新打开的页面
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])

    #找到点赞按钮并点击
    driver.find_element(By.CLASS_NAME, 'like').click()

    # 输出用时
    print(round(time.perf_counter()-start))
    time.sleep(3)
    driver.close()