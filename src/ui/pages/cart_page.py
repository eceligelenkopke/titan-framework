from src.ui.locators.cart_page_locators import CartPageLocators
from src.ui.core.base_page import BasePage
from src.api.helpers.config_helpers import ConfigHelper
from selenium.webdriver.common.keys import Keys

class CartPage(CartPageLocators):
    endpoint = '/cart-2'
    def __init__(self):
        self.cart_page_locators = CartPageLocators
        self.base_page = BasePage()
        self.keys = Keys()

    def wait_until_ui_layer_invisible(self):
        self.base_page.wait_until_element_invisible(self.BLOCK_UI_LAYER)

    def go_to_cart_page(self):
        base_url = ConfigHelper().get_base_url()
        cart_page_url = base_url + self.endpoint
        self.base_page.driver.get(cart_page_url)

    def type_a_coupon(self,coupon_code):
        self.base_page.wait_and_send_input(self.COUPON_LINE,coupon_code)

    def click_on_apply_coupon(self):
        self.base_page.wait_and_click(self.APPLY_COUPON_BUTTON)
        self.wait_until_ui_layer_invisible()
    def wait_until_coupon_applied(self):
        self.base_page.wait_until_element_visible(self.COUPON_APPLIED_MESSAGE)
        self.wait_until_ui_layer_invisible()


    def click_on_proceed_to_checkout_button(self):
        self.base_page.wait_and_scroll_until_element_visible(self.PROCEED_TO_CHECKOUT_BUTTON)
        self.base_page.wait_and_click(self.PROCEED_TO_CHECKOUT_BUTTON)

    def get_product_price_from_ui(self):
        self.base_page.wait_and_scroll_until_element_visible(self.PRICE_VALUE)
        return float(self.base_page.get_text_of_element(self.PRICE_VALUE).split('$')[1].replace(',' , ''))

    def get_final_price_value_via_ui(self):
        self.base_page.wait_and_scroll_until_element_visible(self.TOTAL_PRICE)
        return float(self.base_page.get_text_of_element(self.TOTAL_PRICE).split('$')[1].replace(',' , ''))

    def get_existing_quantity_value(self):
       return int(self.base_page.get_attribute_of_element(self.QUANTITY_LINE,"value"))

    def delete_existing_quantity_value(self):
        self.wait_until_ui_layer_invisible()
        backspace_input = self.keys.BACKSPACE
        self.base_page.wait_and_click(self.QUANTITY_LINE)
        self.base_page.wait_and_send_input(self.QUANTITY_LINE,backspace_input)

    def update_quantity_value(self,quantity_value):
        input_enter = self.keys.ENTER
        self.base_page.wait_and_send_input(self.QUANTITY_LINE,quantity_value)
        self.base_page.wait_and_send_input(self.QUANTITY_LINE,input_enter)
        self.wait_until_ui_layer_invisible()

    def click_on_update_cart_button(self):
        self.wait_until_ui_layer_invisible()
        self.base_page.wait_until_element_clickable(self.UPDATE_CART_BUTTON)
        self.base_page.wait_and_click(self.UPDATE_CART_BUTTON)


    def wait_until_cart_updated_message_visible(self):
        self.base_page.wait_until_element_visible(self.CART_UPDATED_MESSAGE)

    def remove_product_from_cart(self):
        self.base_page.wait_until_element_visible(self.REMOVE_ITEM_BUTTON)
        self.base_page.wait_and_click(self.REMOVE_ITEM_BUTTON)
        self.wait_until_ui_layer_invisible()

    def get_product_name_via_ui(self):
        self.base_page.wait_until_element_visible(self.CART_PAGE_PRODUCT_NAME)
        return self.base_page.get_text_of_element(self.CART_PAGE_PRODUCT_NAME)

    def get_product_remove_message(self):
        self.base_page.wait_until_element_visible(self.PRODUCT_REMOVED_MESSAGE)
        return self.base_page.get_text_of_element(self.PRODUCT_REMOVED_MESSAGE)

    def get_cart_empty_message(self):
        self.base_page.wait_and_scroll_until_element_visible(self.CART_EMPTY_MESSAGE)
        return self.base_page.get_text_of_element(self.CART_EMPTY_MESSAGE)

    def get_invalid_coupon_message(self):
        return self.base_page.get_text_of_element(self.INVALID_COUPON_MESSAGE)
    def get_coupon_usage_limit_message(self):
        return self.base_page.get_text_of_element(self.COUPON_LIMIT_MESSAGE)