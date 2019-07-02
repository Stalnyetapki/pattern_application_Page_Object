from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def press_button_add_in_basket(self):
        button_add_in_basket = self.driver.find_element(*ProductPageLocators.BUTTON_ADD_IN_BASKET)
        button_add_in_basket.click()
#        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
#        self.solve_quiz_and_get_code()

    def should_be_product_name_in_adding_message(self):
        product = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_in_message = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product.text in name_in_message.text, f"added {product.text}, but in basket added {name_in_message.text}"

    def should_be_price_of_product_in_basket_value(self):
        price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_in_message = self.driver.find_element(*ProductPageLocators.PRICE_IN_MESSAGE)
        assert price.text in price_in_message.text, f"product price does not match basket price"
