from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # возвращать нужный Page Object
        # return LoginPage(driver=self.driver, url=self.driver.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
