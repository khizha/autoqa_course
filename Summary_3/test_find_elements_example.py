from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from urls import CAT_MEMES
from time import time
from locators import xpath_id_cat_bullet, xpath_name_cat_vova

#driver = webdriver.Chrome()
#driver.get("https://the-internet.herokuapp.com/forgot_password")
#
#form = driver.find_element(By.CSS_SELECTOR, "#forgot_password")
#print(form.text)
#
#element_by_xpath = driver.find_element(By.XPATH, '//*[@id="form_submit"]')
#print(element_by_xpath.text)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(CAT_MEMES)
    yield driver
    driver.quit()


# def test_displayed_cat_bullet(driver):
#     cat_bullet = driver.find_element(By.XPATH, xpath_id_cat_bullet)
#     assert cat_bullet.is_displayed() is True
#
# def test_displayed_cat_name_vova(driver):
#     cat_vova = driver.find_element(By.XPATH, xpath_name_cat_vova)
#     assert cat_vova.is_displayed() is True
#
# def test_find_all_cats(driver):
#     cats = driver.find_elements(By.CLASS_NAME, "box-shadow")
#     assert 'Lenin cat' in (cats[3].text)
#     #print(type(cats[3].text))
#
# def test_find_title(driver):
#     title = driver.find_element(By.CLASS_NAME, "jumbotron-heading")
#     # print(title.text)
#     assert 'Cat memes' == title.text
#
# def test_find_title_by_tag(driver):
#     title_text = driver.find_element(By.TAG_NAME, 'h1').text
#     assert title_text == 'Cat memes'
#
# def test_find_all_cats_9mins(driver):
#     cats = driver.find_elements(By.CLASS_NAME, "box-shadow")
#     assert '9 mins' in (cats[1].text)
#
# def test_last_cat_card_name(driver):
#     last_card_name = driver.find_element(By.CSS_SELECTOR,".col-sm-4:nth-child(6) p")
#     assert last_card_name.text == "I love you so much"
#
# def test_cats_album_text(driver):
#     cats_album = driver.find_element(By.TAG_NAME,"strong")
#     assert cats_album.text == "Cats album"

# def test_cats_album_text_near_camera_item(driver):
#     cats_album = driver.find_element(By.TAG_NAME,"strong")
#     assert cats_album.text == "Cats album"


def test_login():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    pwd_field = driver.find_element(By.ID, "password")
    pwd_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element((By.CLASS_NAME, 'fa-sign-in'))
    login_button.click()
    
    time.sleep(5)

    assert driver.find_element(
        By.XPATH,
        "//h4[text()='Welcome to the Secure Area. When you are done click logout below.']"
    )


