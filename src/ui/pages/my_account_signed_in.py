from src.ui.core.base_page import BasePage
from src.ui.locators.my_acc_signed_in_locators import MyAccountSignedInLocators
class MyAccountSignedInPage(MyAccountSignedInLocators):
    def __init__(self):
        self.base_page = BasePage()

    def verify_signed_in_by_acc_details_button(self):
        try:
            self.base_page.wait_until_element_visible(self.ACC_DETAILS_BUTTON)
            return True
        except:
            return False
    def click_on_log_out_button(self):
        self.base_page.wait_until_element_visible(self.LOG_OUT_BUTTON)
        self.base_page.wait_and_click(self.LOG_OUT_BUTTON)

    def go_to_home_page_from_signed_in_page(self):
        self.base_page.wait_until_element_visible(self.WEBSITE_TITLE)
        self.base_page.wait_and_click(self.WEBSITE_TITLE)
