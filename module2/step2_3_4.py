from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x_value = x_element.text
    y = calc(x_value)

    answer_bar = browser.find_element(By.NAME, "text")
    answer_bar.send_keys(y)

    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
