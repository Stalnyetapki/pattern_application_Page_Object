from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_cart(driver):
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.press_button_add_in_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_name_in_adding_message()
    product_page.should_be_price_of_product_in_basket_value()



