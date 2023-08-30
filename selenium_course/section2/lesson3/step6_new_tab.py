from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element(By.ID, "input_value").text)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(calc(x))

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()