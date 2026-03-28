from src.ui.locators.checkout_page_locators import CheckoutPageLocators
from src.ui.core.base_page import BasePage
from src.api.helpers.config_helpers import ConfigHelper
from src.api.helpers.general_helpers import create_random_string
from src.api.helpers.general_helpers import generate_random_email
class CheckOutPage(CheckoutPageLocators):
    endpoint = '/checkout-2'
    def __init__(self):
        self.base_page = BasePage()
        self.config_helper = ConfigHelper()
    def go_to_checkout_page(self):
        base_url = self.config_helper.get_base_url()
        checkout_page_url = base_url + self.endpoint
        self.base_page.driver.get(checkout_page_url)

    def wait_until_ui_layer_invisible(self):
        self.base_page.wait_until_element_invisible(self.BLOCK_UI_LAYER)

    def type_billing_credentials(self,first_name=None,last_name=None,street=None,town=None,zip_code=None,email=None):
        if not email:
            email = generate_random_email()
        if not first_name:
            first_name = create_random_string()
        if not last_name:
            last_name = create_random_string()
        if not street:
            street = create_random_string()
        if not town:
            town = create_random_string()
        if not zip_code:
            zip_code = 12345
        self.base_page.wait_and_send_input(self.BILLING_FIRST_NAME,first_name)
        self.base_page.wait_and_send_input(self.BILLING_LAST_NAME,last_name)
        self.base_page.wait_and_send_input(self.STREET_ADDRESS_LINE_ONE,street)
        self.base_page.wait_and_send_input(self.TOWN_CITY_LINE,town)
        self.base_page.wait_and_send_input(self.ZIP_CODE_LINE,zip_code)
        email_value = self.base_page.get_attribute_of_element(self.BILLING_EMAIL_LINE, "value")

        if not email_value or email_value.strip() == "":
            self.base_page.wait_and_send_input(self.BILLING_EMAIL_LINE,email)
        else:
            pass
    def click_on_place_order_button(self):
        self.wait_until_ui_layer_invisible()
        self.base_page.wait_and_scroll_until_element_visible(self.PLACE_ORDER_BUTTON)
        self.base_page.wait_and_click(self.PLACE_ORDER_BUTTON)
        self.wait_until_ui_layer_invisible()


    def get_order_received_message(self):
        self.base_page.wait_until_element_visible(self.ORDER_RECEIVED_MESSAGE)
        return self.base_page.get_text_of_element(self.ORDER_RECEIVED_MESSAGE)

    def get_order_number(self):
        self.base_page.wait_and_scroll_until_element_visible(self.ORDER_NUMBER)
        return int(self.base_page.get_text_of_element(self.ORDER_NUMBER))

    def get_out_of_stock_message(self):
        self.wait_until_ui_layer_invisible()
        self.base_page.wait_until_element_visible(self.OUT_OF_STOCK_MESSAGE)
        return self.base_page.get_text_of_element(self.OUT_OF_STOCK_MESSAGE)

    def get_checkout_order_price(self):
        self.base_page.wait_until_element_visible(self.CHECKOUT_PRICE_VALUE)
        price_text =  self.base_page.get_text_of_element(self.CHECKOUT_PRICE_VALUE)
        order_price = float(price_text.replace("$",'').replace(',',''))
        return order_price