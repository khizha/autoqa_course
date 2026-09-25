from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_text_input(driver):
    driver.get("http://uitestingplayground.com/textinput")

    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    assert button.text == "ITCH"
