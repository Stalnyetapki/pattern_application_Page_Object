from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def take_product_name(self):
        product = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product.text

    def take_product_price(self):
        price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price.text

    def press_button_add_in_basket(self):
        button_add_in_basket = self.driver.find_element(*ProductPageLocators.BUTTON_ADD_IN_BASKET)
        button_add_in_basket.click()

    def should_be_product_name_in_adding_message(self, name):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME)
        product = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        name_in_message = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product.text == name_in_message.text, f"{product.text} does not match {name_in_message.text}"
        assert name == name_in_message.text, f"added {name} on adding page, but in basket added {name_in_message.text}"
        assert name == product.text, f"added {name} on adding page, but after name of product was {product.text}"

    def should_be_price_of_product_in_basket_value(self, price):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)
        product_price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_MESSAGE)
        price_in_message = self.driver.find_element(*ProductPageLocators.PRICE_IN_MESSAGE)
        assert product_price.text == price_in_message.text, "product price does not match basket price"
        assert price == price_in_message.text, \
            "product price on adding page does not match basket price when product added"
        assert price == product_price.text, f"{price} != {product_price}"
