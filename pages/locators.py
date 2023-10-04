from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    PRODUCT_WAS_ADDED_TO_BASKET = SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BASKET_MINI = (By.CLASS_NAME, 'basket-mini')

class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')
    MSG_ABOUT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, 'div#content_inner p')