from src.selenium.core.webdriver_provider import WebDriverProvider
from src.api.helpers.config_helpers import ConfigHelper
from src.ui.locators.my_acc_signed_out_locators import MyAccSignedOutLocators
from src.ui.core.base_page import BasePage
import pytest

class MyAccountSignedOutPage(MyAccSignedOutLocators):
    endpoint = "/my-account-2"
    def __init__(self):
        self.base_page = BasePage()
        self.page_locators = MyAccSignedOutLocators()
    def go_to_my_acc_signed_out_page(self):
        base_url = ConfigHelper.get_base_url()
        my_acc_url = base_url + self.endpoint
        self.base_page.driver.get(my_acc_url)

    def type_login_username(self,username):
        self.base_page.wait_and_send_input(self.LOGIN_USERNAME_BLANK,username)
    def type_login_password(self,password):
        self.base_page.wait_and_send_input(self.LOGIN_PASSWORD_BLANK,password)
    def click_on_login_button(self):
        self.base_page.wait_and_click(self.LOGIN_BUTTON)
    def scroll_until_login_button_seen(self):
        try:
            self.base_page.wait_and_scroll_until_element_visible(self.LOGIN_BUTTON)
            return True
        except:
            return False
    def get_invalid_login_error_username(self):
        return self.base_page.get_text_of_element(self.INVALID_LOGIN_ERROR)
    def get_invalid_login_error_email(self):
        return self.base_page.get_text_of_element(self.INVALID_LOGIN_ERROR_EMAIL)
    def type_register_email(self,email):
        self.base_page.wait_and_send_input(self.REGISTER_EMAIL_BLANK,email)

    def type_register_password(self,password):
        self.base_page.wait_and_send_input(self.REGISTER_PASSWORD_BLANK,password)

    def scroll_until_register_button_visible(self):
        self.base_page.wait_and_scroll_until_element_visible(self.REGISTER_BUTTON)

    def get_register_title(self):
        return self.base_page.get_text_of_element(self.REGISTER_TITLE)
    def click_on_register_button(self):
        self.base_page.wait_and_click(self.REGISTER_BUTTON)
