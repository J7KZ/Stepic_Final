import math

import pytest
from selenium.common.exceptions import NoAlertPresentException

from pages.basket_page import BasketPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
# link1="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

class TestUserAddToBasketFromProductPage():
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


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in [*range(0,7),pytest.param(7, marks=pytest.mark.xfail), *range(8,10)]]
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
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

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open_page()
    page.should_be_btn_add_to_basket()
    page.add_to_basket()
    page.should_not_be_success_message()



def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open_page()
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

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open_page()
    page.should_be_login_link()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open_page()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items()
    basket_page.should_be_msg_about_basket_is_empty()