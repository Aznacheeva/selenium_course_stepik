from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")
    valuex = int(treasure.get_attribute("valuex"))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(valuex))

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()