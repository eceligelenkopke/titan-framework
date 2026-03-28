from selenium.webdriver.common.by import By
class MyAccountSignedInLocators:
    ACC_DETAILS_BUTTON = By.CSS_SELECTOR,'li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--edit-account'
    LOG_OUT_BUTTON = By.CSS_SELECTOR,'li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a'
    WEBSITE_TITLE = By.CSS_SELECTOR,'div.col-lg-3.col-md-5.col-sm-5.col-12.align-self-center > div > p > a'
