from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.ie.webdriver import WebDriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_about_button(driver: WebDriver):
    driver.get("https://itcareerhub.de/ru")
    about_button = driver.find_element(By.LINK_TEXT, "О нас")
    about_button.click()
    about_company = driver.find_element(By.LINK_TEXT, "О компании")
    print(about_company.text)
    assert about_company.text == 'О компании'