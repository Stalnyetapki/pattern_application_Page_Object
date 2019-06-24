from .pages.login_page import LoginPage


def test_existence_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(driver, link)
    page.open()
    page.should_be_login_page()
