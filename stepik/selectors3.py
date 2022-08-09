import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


url = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    inputs = browser.find_elements(By.TAG_NAME, 'input')
    # action = ActionChains(browser)

    for input in inputs:
        input.send_keys("@")
        # action.move_to_element(input).perform()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()