from src.ui.locators.product_page_locators import ProductPageLocators
from src.ui.core.base_page import BasePage
from src.api.helpers.config_helpers import ConfigHelper
from src.api.helpers.general_helpers import create_random_string,generate_random_email

class ProductPage(ProductPageLocators):
    endpoint = 'product/'
    def __init__(self):
        self.base_page = BasePage()
        self.product_page_locators = ProductPageLocators()

    def go_to_product_page_by_slug(self,slug):
        base_url = ConfigHelper.get_base_url()
        product_page_url = base_url + self.endpoint + slug
        self.base_page.driver.get(product_page_url)
    def click_on_add_to_cart_button(self):
        self.base_page.wait_until_element_visible(self.PRODUCT_PAGE_ADD_TO_CART_BUTTON)
        self.base_page.wait_and_click(self.PRODUCT_PAGE_ADD_TO_CART_BUTTON)
    def wait_until_added_to_cart_message(self):
        self.base_page.wait_until_element_visible(self.PRODUCT_PAGE_ADDED_TO_CART_MESSAGE)
    def get_added_to_cart_message(self):
        return self.base_page.get_text_of_element(self.PRODUCT_PAGE_ADDED_TO_CART_MESSAGE)

    def product_title_in_product_page(self):
        return self.base_page.get_text_of_element(self.PRODUCT_PAGE_PRODUCT_TITLE).lower()
    def click_on_view_cart_button(self):
        self.base_page.wait_until_element_visible(self.PRODUCT_PAGE_VIEW_CART_BUTTON)
        self.base_page.wait_and_click(self.PRODUCT_PAGE_VIEW_CART_BUTTON)

    def click_on_review_button(self):
        self.base_page.wait_and_scroll_until_element_visible(self.PRODUCT_PAGE_REVIEW_BUTTON)
        self.base_page.wait_and_click(self.PRODUCT_PAGE_REVIEW_BUTTON)

    def give_stars(self):
        self.base_page.wait_and_scroll_until_element_visible(self.PRODUCT_PAGE_STARS)
        self.base_page.wait_and_click(self.PRODUCT_PAGE_STARS)

    def make_a_comment(self,comment):
        if not comment:
            comment = create_random_string(string_length=20)
        self.base_page.wait_and_scroll_until_element_visible(self.COMMENT_LINE)
        self.base_page.wait_and_click(self.COMMENT_LINE)
        self.base_page.wait_and_send_input(self.COMMENT_LINE,comment)

    def type_comment_name(self,name):
        if not name:
            name = create_random_string(string_length=5)
        self.base_page.wait_and_scroll_until_element_visible(self.REVIEW_NAME_LINE)
        self.base_page.wait_and_click(self.REVIEW_NAME_LINE)
        self.base_page.wait_and_send_input(self.REVIEW_NAME_LINE,name)

    def type_comment_email(self,email):
        if not email:
            email = generate_random_email()
        self.base_page.wait_and_scroll_until_element_visible(self.REVIEW_EMAIL_LINE)
        self.base_page.wait_and_click(self.REVIEW_EMAIL_LINE)
        self.base_page.wait_and_send_input(self.REVIEW_EMAIL_LINE,email)
    def click_on_submit_button(self):
        self.base_page.wait_and_scroll_until_element_visible(self.REVIEW_SUBMIT_BUTTON)
        self.base_page.wait_and_click(self.REVIEW_SUBMIT_BUTTON)
    def review_waiting_approval_message(self):
        self.base_page.wait_until_element_visible(self.AWAITING_APPROVAL_MESSAGE)
        return self.base_page.get_text_of_element(self.AWAITING_APPROVAL_MESSAGE)
    def get_review_message_text(self):
        self.base_page.wait_until_element_visible(self.REVIEW_MESSAGE)
        return self.base_page.get_text_of_element(self.REVIEW_MESSAGE)
    def get_product_page_price(self):
        self.base_page.wait_until_element_visible(self.PRODUCT_PAGE_PRICE)
        return float(self.base_page.get_text_of_element(self.PRODUCT_PAGE_PRICE).split('$')[1].replace(',' , ''))
