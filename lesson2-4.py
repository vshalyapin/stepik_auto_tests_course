from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math, time
from selenium import webdriver

from selenium.webdriver.support.ui import Select

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button = browser.find_element(By.ID, "book")
button.click()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.NAME,"text")
input1.send_keys(y)

option4 = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
option4.click()

time.sleep(5)
browser.quit()

# не забываем оставить пустую строку в конце файла