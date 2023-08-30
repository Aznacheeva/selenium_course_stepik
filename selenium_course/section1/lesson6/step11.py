from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_web_element_by_template(type_input):
    return browser.find_element(By.CSS_SELECTOR, "input[placeholder=\"Input your {}\"]".format(type_input))

link = "https://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try: 
    
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    # Заполняем имя
    first_name_input = get_web_element_by_template("first name")
    first_name_input.send_keys("Ivan")

    # Заполняем фамилию
    last_name_input = get_web_element_by_template("last name")
    last_name_input.send_keys("Petrov")

    # Заполняем почту
    email_input = get_web_element_by_template("email")
    email_input.send_keys("mail@mail.com")

    # Смотрим, что получилось
    time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

