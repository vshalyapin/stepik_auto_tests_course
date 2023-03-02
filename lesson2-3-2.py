from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math, time
from selenium import webdriver

from selenium.webdriver.support.ui import Select

import os

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME,"button")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID,'input_value')
x = x_element.text
y = calc(x)

element1 = browser.find_element(By.ID,'answer')
element1.send_keys(y)

option4 = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
option4.click()

time.sleep(5)
browser.quit()

# не забываем оставить пустую строку в конце файла