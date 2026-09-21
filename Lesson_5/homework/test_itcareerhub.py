from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(ITCAREERHUB)
    yield driver
    driver.quit()


def test_itcareerhub(driver):

    # Проверяем логотип
    assert driver.find_element(By.XPATH, logo).is_displayed()

    # Проверяем пункты меню
    assert driver.find_element(By.XPATH, programs).is_displayed()
    assert driver.find_element(By.XPATH, payment_methods).is_displayed()
    assert driver.find_element(By.XPATH, about).is_displayed()
    assert driver.find_element(By.XPATH, reviews).is_displayed()
    assert driver.find_element(By.XPATH, blog).is_displayed()

    # Проверяем языки
    assert driver.find_element(By.XPATH, language_ru).is_displayed()
    assert driver.find_element(By.XPATH, language_de).is_displayed()

    # Переходим в раздел "О нас"
    driver.find_element(By.XPATH, about).click()

    # Переходим в "Контакты"
    driver.find_element(By.XPATH, contacts).click()

    # Ждём появления кнопки
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.XPATH, callback).is_displayed()
    )

    # Нажимаем "Обратный звонок"
    driver.find_element(By.XPATH, callback).click()

    # Проверяем текст во всплывающем окне
    assert driver.find_element(
        By.XPATH,
        consultation_text
    ).is_displayed()