from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


import time



url = 'http://suninjuly.github.io/selects2.html'

with webdriver.Chrome() as browser:
    browser.get(url=url)

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    #  eq = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/label/span[1]').text.split(',')[0].split(' ')[-1]
    res = num1 + num2
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))

    
    time.sleep(2)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


    time.sleep(20)