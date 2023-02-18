from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x,y):
  return str(int(x)+int(y))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    x_element = browser.find_element(By.ID, "num1").text
    y_element = browser.find_element(By.ID, "num2").text
    sum = calc(x_element,y_element)
    print(int(x_element)+int(y_element))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)  # ищем элемент с текстом "Python"

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
