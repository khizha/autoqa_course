"""
Открыть страницу Drag & Drop Demo.
Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.

Выполнить следующие шаги:

Захватить первую фотографию (верхний левый элемент).
Перетащить её в область корзины (Trash).
Проверить, что после перемещения:
    В корзине появилась одна фотография.
    В основной области осталось 3 фотографии.

Ожидаемый результат:
    Фотография успешно перемещается в корзину.
    Вне корзины остаются 3 фотографии.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


@pytest.fixture
def browser():
    """Создает и закрывает браузер после теста."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_drag_and_drop(browser):
    browser.get("https://www.globalsqa.com/demo-site/draganddrop/")

    iframe = browser.find_element(By.CSS_SELECTOR, "iframe[src*='photo-manager']")
    browser.switch_to.frame(iframe)

    photo = browser.find_element(By.XPATH, '//ul[@id="gallery"]/li[1]')
    trash = browser.find_element(By.ID, 'trash')

    actions = ActionChains(browser)
    actions.drag_and_drop(photo, trash).perform()

    time.sleep(2)

    # Проверяем количество фотографий в корзине
    photos_in_trash = len(
        browser.find_elements(
            By.XPATH,
            "//div[@id='trash']//ul/li"
        )
    )

    # Проверяем количество фотографий в галерее
    photos_in_gallery = len(
        browser.find_elements(
            By.XPATH,
            "//ul[@id='gallery']/li"
        )
    )

    assert photos_in_trash == 1
    assert photos_in_gallery == 3
