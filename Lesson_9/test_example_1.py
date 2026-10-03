"""
http://suninjuly.github.io/huge_form.html
Заполнить все поля ввода
Найти все input-поля типа text внутри формы.
Ввести в каждое поле значение "Hello".
Нажать кнопку Submit
Найти кнопку с классом btn btn-default.
Нажать на неё.
Дождаться появления Alert
Переключиться на всплывающее окно (alert).
Проверить текст Alert
Получить текст из alert.
Убедиться, что он содержит строку "Congrats, you've passed the task!".
"""
from calendar import firstweekday

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_fill_form_and_chack_alert(browser):
    url = 'http://suninjuly.github.io/huge_form.html'
    browser.get(url)
    input_feilds = browser.find_elements(By.TAG_NAME, 'input')
    for field in input_feilds:
        field.clear()
        field.send_keys("Hello")

    submit_button = browser.find_element(By.CLASS_NAME, 'btn-default')
    submit_button.click()

    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    # alert_text = Alert(browser).text
    alert_text = browser.switch_to.alert.text

    expected_substring = "Congrats, you've passed the task!"
    assert expected_substring in alert_text
    alert.accept()

"""
https://suninjuly.github.io/math.html
Вычислить математическое выражение
Найти выражение на странице.
Посчитать его значение.
Ввести полученный результат в поле ввода.
Выбрать чекбокс
Установить флажок "I'm the robot".
Выбрать радиокнопку
Кликнуть по радио-кнопке "Robots rule".
Отправить форму
Нажать на кнопку "Submit".
Проверить Alert
Дождаться появления всплывающего окна (alert).
Проверить, что текст alert содержит "Congrats, you've passed the task!".
"""

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def test_math_form(browser):
    url = 'https://suninjuly.github.io/math.html'
    browser.get(url)
    x_value = browser.find_element(By.ID, 'input_value')
    result = calc(x_value.text)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.clear()
    answer_input.send_keys(result)

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robot_rule_radio = browser.find_element(By.ID, "robotsRule")
    robot_rule_radio.click()

    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = Alert(browser).text
    expected_substing = "Congrats, you've passed the task!"
    assert expected_substing in alert_text
    time.sleep(5)
    alert.accept()