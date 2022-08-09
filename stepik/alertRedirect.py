# new_window = browser.window_handles[1]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/redirect_accept.html"


with webdriver.Chrome() as browser:
    browser.get(url=url)

    browser.find_element(By.TAG_NAME, "button").click()

    time.sleep(.5)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # browser.switch_to.alert.accept()

    time.sleep(.5)

    x = int(browser.find_element(By.ID, 'input_value').text)

    res = calc(x)

    # first name
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(str(res))
    # last name
    # browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys("Truedaux")
    # email
    # browser.find_element(By.XPATH, '//input[@name="email"]').send_keys("cat@mice.fr")

    time.sleep(.5)
    # file
    # browser.find_element(By.ID, 'file').send_keys(file_path)


    # button
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(20)