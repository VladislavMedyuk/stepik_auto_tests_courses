import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    link = browser.find_element(By.PARTIAL_LINK_TEXT, "224592")
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Vladosik")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Medyuk")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Minsk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Belarus")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
