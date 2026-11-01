from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )


    def add_item_to_cart(self, item_name):
        items = self.get_items()

        for item in items:
            name = item.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text

            if name == item_name:
                button = item.find_element(
                    By.TAG_NAME, "button"
                )

                button.click()

                break


    def go_to_cart(self):
        cart_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )

        cart_button.click()