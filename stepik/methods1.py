from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = 'https://suninjuly.github.io/math.html'

with webdriver.Chrome() as browser:
    browser.get(url=url)

    x = int(browser.find_element(By.ID, 'input_value').text)
    #  eq = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/label/span[1]').text.split(',')[0].split(' ')[-1]
    res = calc(x)
    
    browser.find_element(By.ID, 'answer').send_keys(res)

    browser.find_element(By.ID, 'robotCheckbox').click()

    browser.find_element(By.ID, 'robotsRule').click()
    time.sleep(.5)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


    time.sleep(20)