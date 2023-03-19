import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element(By.ID, "input_value").text
    y = calc(x_value)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 100);")

    answer_bar = browser.find_element(By.ID, "answer")
    answer_bar.send_keys(y)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "[value = 'robots']").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()



finally:
    time.sleep(5)
    browser.quit()
