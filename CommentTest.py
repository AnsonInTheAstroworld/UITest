import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import Cookies

# 获取cookies，以绕过测试中的登录
url = "https://www.bilibili.com/"
cookies = Cookies.getCookies(url)

for i in range(0,10):
    # 记录开始时间
    start=time.perf_counter()

    driver=webdriver.Chrome()
    driver.get(url)
    # 绕过登录
    Cookies.addCookies(driver,cookies)

    driver.find_element(By.CLASS_NAME, 'recommended-card').click()

    # 转到新打开的页面
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])

    # 找到评论输入框并输入
    WebDriverWait(driver, 5, 1).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="comment"]//textarea')))
    driver.find_element(By.XPATH, '//*[@id="comment"]//textarea').send_keys('up好厉害！')
    driver.find_element(By.CLASS_NAME, 'send-text').click()

    print(round(time.perf_counter()-start))
    time.sleep(3)
    driver.close()