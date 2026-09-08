from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://itcareerhub.de/ru")

# Закрываем cookies
driver.find_element(By.XPATH, "//span[text()='Accept all']").click()
time.sleep(3)

# Переходим в "Способы оплаты"
payment_methods_button = driver.find_element(By.LINK_TEXT, "Способы оплаты")
payment_methods_button.click()
time.sleep(3)

# делаем скриншот
driver.save_screenshot("./screenshot.png")
time.sleep(3)

driver.quit()
