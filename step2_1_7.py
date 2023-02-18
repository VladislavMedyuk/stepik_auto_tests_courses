from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element(By.ID, "treasure")
    x_value = x_element.get_attribute("valuex")
    y = calc(x_value)

    answer_bar = browser.find_element(By.ID, "answer")
    answer_bar.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
