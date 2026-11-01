from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_checkout_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        )

    def click_on_checkout_button(self):
        self.get_checkout_button().click()