from src.ui.locators.home_page_locators import HomePageLocators
from src.ui.core.base_page import BasePage
from src.api.helpers.config_helpers import ConfigHelper
from selenium.webdriver.common.keys import Keys
class HomePage(HomePageLocators):
    endpoint = "/"
    def __init__(self):
        self.base_page = BasePage()
        self.home_page_locators = HomePageLocators()

    def go_to_home_page(self):
        base_url = ConfigHelper.get_base_url()
        home_page_url = base_url + self.endpoint
        self.base_page.driver.get(home_page_url)

    def go_to_home_page_clicking(self):
        self.base_page.wait_and_click(self.WEBSITE_TITLE)

    def scroll_until_finding_product(self):
        self.base_page.wait_and_scroll_until_element_visible(self.ADD_TO_CART_BTN)

    def click_on_add_to_cart_button(self):
        self.base_page.wait_and_click(self.ADD_TO_CART_BTN)

    def wait_until_cart_updated(self):
        self.base_page.wait_until_element_visible(self.VIEW_CART_BUTTON)

    def click_on_view_cart_button(self):
        self.base_page.wait_and_scroll_until_element_visible(self.VIEW_CART_BUTTON)
        self.base_page.wait_and_click(self.VIEW_CART_BUTTON)

    def click_on_a_product(self):
        self.base_page.wait_and_scroll_until_element_visible(self.PRODUCT_SELECTOR)
        self.base_page.wait_and_click(self.PRODUCT_PRICE)


    def scroll_back_to_my_cart_section(self):
        self.base_page.wait_and_scroll_until_element_visible(self.MY_CART_BTN)

    def get_product_amount_in_cart(self):
        product_amount_in_cart = self.base_page.get_text_of_element(self.CART_VALUE)
        return int(product_amount_in_cart)

    def click_on_search_products(self):
        self.base_page.wait_and_click(self.SEARCH_FIELD)

    def search_a_product(self,product_name):
        self.base_page.wait_and_send_input(self.SEARCH_FIELD,product_name)

    def click_on_search_button(self):
        self.base_page.wait_and_click(self.SEARCH_BTN)

    def get_product_title(self):
        return self.base_page.get_text_of_element(self.PRODUCT_TITLE).lower()

    def get_search_results_message(self):
        self.base_page.wait_and_scroll_until_element_visible(self.SEARCH_RESULTS_BAR)
        return self.base_page.get_text_of_element(self.SEARCH_RESULTS_BAR)
    def get_no_product_found_message(self):
        return self.base_page.get_text_of_element(self.NO_PRODUCT_FOUND_MESSAGE)

    def go_to_shop_by_category(self):
        self.base_page.wait_and_click(self.SHOP_BY_CATEGORY_TOP_BAR)

    def click_on_about_me_side_bar(self):
        self.base_page.wait_and_scroll_until_element_visible(self.ABOUT_ME_BUTTON_SIDE_BAR)
        self.base_page.wait_until_element_clickable(self.ABOUT_ME_BUTTON_SIDE_BAR)
        self.base_page.wait_and_click(self.ABOUT_ME_BUTTON_SIDE_BAR)

    def scroll_and_register_to_newsletter(self,email):
        self.base_page.wait_and_scroll_until_element_visible(self.NEWSLETTER_SIGN_UP_INPUT_BLANK)
        self.base_page.wait_and_click(self.NEWSLETTER_SIGN_UP_INPUT_BLANK)
        self.base_page.wait_and_send_input(self.NEWSLETTER_SIGN_UP_INPUT_BLANK,email)
        self.base_page.wait_and_send_input(self.NEWSLETTER_SIGN_UP_INPUT_BLANK,Keys.ENTER)
    def get_newsletter_success_message(self):
        self.base_page.wait_until_element_visible(self.NEWSLETTER_SUCCESS_MESSAGE)
        return self.base_page.get_text_of_element(self.NEWSLETTER_SUCCESS_MESSAGE)
