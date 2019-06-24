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
