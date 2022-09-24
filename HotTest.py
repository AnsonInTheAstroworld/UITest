import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

for i in range(0,10):
    start=time.perf_counter()
    driver=webdriver.Chrome()
    driver.get('https://www.bilibili.com/')

    # 找到热门按钮
    WebDriverWait(driver, 5, 1).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, 'channel-icons__item')))
    driver.find_elements(By.CLASS_NAME,'channel-icons__item')[1].click()

    # 转到新打开的页面
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])

    # 找到第一个热门视频
    WebDriverWait(driver, 5, 1).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/div[1]/div[1]/a/img')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/ul/div[1]/div[1]/a/img').click()

    print(round(time.perf_counter()-start))
    driver.close()