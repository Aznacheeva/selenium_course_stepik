from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x = int(browser.find_element(By.ID, "input_value").text)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(calc(x))

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()

