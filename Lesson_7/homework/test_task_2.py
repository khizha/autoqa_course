from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_loading_images(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 10)

    # ждем, пока на странице появится изображение с alt="award"
    third_image = wait.until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='award']"))
    )

    assert third_image.get_attribute("alt") == "award"
