from selenium.webdriver.common.by import By

from .pages.main_page import MainPage
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):

    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

    # browser.get(link)
    # login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    # login_link.click()


def test_guest_should_see_login_link(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_login_link()
