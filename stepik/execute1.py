from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



url = "https://SunInJuly.github.io/execute_script.html"


with webdriver.Chrome() as browser:
    browser.get(url=url)

    x = int(browser.find_element(By.ID, 'input_value').text)
    res = calc(x)
    
    browser.find_element(By.ID, 'answer').send_keys(res)

    browser.find_element(By.ID, 'robotCheckbox').click()


    radio_btn = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_btn)
    radio_btn.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


    time.sleep(20)