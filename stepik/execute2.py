from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'mybio.txt')           # добавляем к этому пути имя файла 



url = "http://suninjuly.github.io/file_input.html"


with webdriver.Chrome() as browser:
    browser.get(url=url)

    # first name
    browser.find_element(By.XPATH, '//input[@name="firstname"]').send_keys("Jerome")
    # last name
    browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys("Truedaux")
    # email
    browser.find_element(By.XPATH, '//input[@name="email"]').send_keys("cat@mice.fr")

    time.sleep(1)
    # file
    browser.find_element(By.ID, 'file').send_keys(file_path)


    # button
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(20)