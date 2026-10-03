import time

import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Lesson_1.test_calculator import result


# Фикстура для WebDriver
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Функция для вычисления выражения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_redirect_and_math(browser):
    url = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(url)
    time.sleep(5)
    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    x_value = browser.find_element(By.ID, 'input_value').text
    result = calc(x_value)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = Alert(browser).text
    expected_alert_text = "Congrats, you've passed the task!"
    assert expected_alert_text in alert_text
    time.sleep(5)
    alert.accept()