from  Lesson_11.homework.pages.login_page import LoginPage
from  Lesson_11.homework.pages.inventory_page import InventoryPage
from  Lesson_11.homework.pages.cart_page import CartPage
from  Lesson_11.homework.pages.checkout_page import CheckoutPage


def test_checkout_total(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Авторизация
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_on_login_button()

    # Добавление товаров в корзину
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_item_to_cart("Sauce Labs Onesie")

    # Переход в корзину и оформление заказа
    inventory_page.go_to_cart()

    cart_page.click_on_checkout_button()

    # Заполнение данных покупателя
    checkout_page.fill_checkout_form(
        "Name",
        "Surname",
        "22222"
    )

    checkout_page.click_on_continue_button()

    # Проверка итоговой суммы
    total_price = checkout_page.get_total_price()

    assert total_price == "Total: $58.29"