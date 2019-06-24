from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()


def go_to_login_page(driver):
    link = driver.find_element_by_css_selector("#login_link")
    link.click()
