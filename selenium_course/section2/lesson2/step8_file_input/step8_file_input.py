from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def get_web_element_by_placeholder(type_input):
    return browser.find_element(By.CSS_SELECTOR, "input[placeholder = \"Enter {}\"]".format(type_input))

def get_file_path(file_name):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(current_dir, file_name)

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Заполняем имя
    first_name_input = get_web_element_by_placeholder("first name")
    first_name_input.send_keys("Ivan")

    # Заполняем фамилию
    last_name_input = get_web_element_by_placeholder("last name")
    last_name_input.send_keys("Petrov")

    # Заполняем почту
    email_input = get_web_element_by_placeholder("email")
    email_input.send_keys("mail@mail.com")

    input_file = browser.find_element(By.ID, "file")
    file_path = get_file_path("text.txt")
    input_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()