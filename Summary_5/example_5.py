from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/droppable/")

    iframe = driver.find_element(By.CLASS_NAME, 'demo-frame')
    driver.switch_to.frame(iframe)

    source = driver.find_element(By.ID, 'draggable')
    target = driver.find_element(By.ID, 'droppable')

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
