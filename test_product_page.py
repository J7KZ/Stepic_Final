import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"

class TestUserAddToBasketFromProductPage():
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    login_link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, self.login_link)
        page.open_page()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, 'test-password')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser, link):
        browser.delete_all_cookies()
        page = ProductPage(browser, link)
        page.open_page()
        page.should_be_btn_add_to_basket()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_price()
        page.should_be_name()
        page.should_product_added_to_basket()
        page.should_be_increased_price_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open_page()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open_page()
    page.should_be_btn_add_to_basket()
    page.add_to_basket()
    page.should_be_price()
    page.should_be_name()
    page.should_product_added_to_basket()
    page.should_be_increased_price_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open_page()
    page.should_be_btn_add_to_basket()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    page = ProductPage(browser, link)
    page.open_page()
    page.add_to_basket()
    page.should_disappear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open_page()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open_page()
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open_page()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items()
    basket_page.should_be_msg_about_basket_is_empty()