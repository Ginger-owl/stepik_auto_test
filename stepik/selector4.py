import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


url = 'http://suninjuly.github.io/find_xpath_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    inputs = browser.find_elements(By.TAG_NAME, 'input')
    # action = ActionChains(browser)

    for input in inputs:
        input.send_keys("Text")
        # action.move_to_element(input).perform()

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    time.sleep(15)
    browser.quit()