from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.google.com"
browser = webdriver.Chrome()

try:
    browser.get(link)

finally:
    time.sleep(10)
    browser.quit()