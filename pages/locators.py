from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    EMAIL_INPUT_LOGIN_FORM = (By.CLASS_NAME, "login-username")
    PASSWORD_INPUT_LOGIN_FORM = (By.CLASS_NAME, "login-password")
    PASSWORD_LINK_LOGIN_FORM = (By.CSS_SELECTOR, "p > a")
    BUTTON_SUBMIT_LOGIN_FORM = (By.CLASS_NAME, "login_submit")

    REGISTRATION_FORM = (By.ID, "register_form")
    EMAIL_INPUT_REGISTRATION_FORM = (By.CLASS_NAME, "registration-email")
    PASSWORD_INPUT_REGISTRATION_FORM = (By.CLASS_NAME, "registration-password1")
    REPEAT_PASSWORD_INPUT_REGISTRATION_FORM = (By.CLASS_NAME, "registration-password2")
    BUTTON_SUBMIT_REGISTRATION_FORM = (By.CLASS_NAME, "registration_submit")


class ProductPageLocators:
    BUTTON_ADD_IN_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) div.alertinner  > strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
