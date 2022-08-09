"""  
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
 """


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

# Открыть страницу
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), text_='100')
    )
button = browser.find_element(By.ID, 'book')
button.click()

WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.ID, "input_value"))
    )
x = int(browser.find_element(By.ID, 'input_value').text)

res = calc(x)

form = browser.find_element(By.ID, 'answer')
form.send_keys(res)

browser.find_element(By.ID, 'solve').click()
time.sleep(10)
