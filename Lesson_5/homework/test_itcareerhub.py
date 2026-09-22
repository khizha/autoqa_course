from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from urls import ITCAREERHUB
from locators import (
    logo,
    programs,
    payment_methods,
    about,
    reviews,
    blog,
    language_ru,
    language_de,
    contacts,
    callback,
    consultation_text
)

import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(ITCAREERHUB)
    yield driver
    driver.quit()


def test_itcareerhub(driver):

    # Проверяем логотип
    assert driver.find_element(By.CSS_SELECTOR, logo).is_displayed()

    # Проверяем пункты меню
    assert driver.find_element(By.LINK_TEXT, programs).is_displayed()
    assert driver.find_element(By.LINK_TEXT, payment_methods).is_displayed()
    assert driver.find_element(By.LINK_TEXT, about).is_displayed()
    assert driver.find_element(By.LINK_TEXT, reviews).is_displayed()
    assert driver.find_element(By.LINK_TEXT, blog).is_displayed()

    # Проверяем языки
    assert driver.find_element(By.CSS_SELECTOR, language_ru).is_displayed()
    assert driver.find_element(By.LINK_TEXT, language_de).is_displayed()

    # Переходим в раздел "О нас"
    driver.find_element(By.PARTIAL_LINK_TEXT, about).click()

    # Переходим в "Контакты"
    driver.find_element(By.PARTIAL_LINK_TEXT, contacts).click()
    # Ждём появления кнопки
    time.sleep(3)

    # Нажимаем "Обратный звонок"
    driver.find_element(By.XPATH, callback).click()

    # Проверяем текст во всплывающем окне
    assert driver.find_element(
        By.XPATH,
        consultation_text
    ).is_displayed()