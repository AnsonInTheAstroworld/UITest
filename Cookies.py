import time

from selenium import webdriver

def getCookies(url):
    driver = webdriver.Chrome()
    driver.get(url)

    # 程序打开网页后20秒内 “手动登陆账户”
    time.sleep(20)

    driver.refresh()
    cookies = driver.get_cookies()
    driver.close()
    return cookies

def addCookies(driver,cookies):
    driver.delete_all_cookies()
    for cookie in cookies:
        cookie_dict = {
            'domain': '.bilibili.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": cookie.get('value'),
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False}
        driver.add_cookie(cookie_dict)
    driver.refresh()