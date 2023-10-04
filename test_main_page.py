import pytest
from selenium.webdriver.common.by import By

from pages.basket_page import BasketPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
        page = MainPage(browser, link)
        page.open_page()
        page.should_be_login_link()


    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        main_page = MainPage(browser, link)
        main_page.open_page()
        main_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items()
        basket_page.should_be_msg_about_basket_is_empty()
