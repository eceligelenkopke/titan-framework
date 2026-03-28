from selenium.webdriver.common.by import By

class MyAccSignedOutLocators:
    LOGIN_USERNAME_BLANK = By.ID,'username'
    LOGIN_PASSWORD_BLANK = By.ID,'password'
    LOGIN_SELECT_REMEMBER_ME = By.ID,'rememberme'
    LOGIN_BUTTON = By.XPATH,'//*[@id="customer_login"]/div[1]/form/p[3]/button'
    LOGIN_LOST_PASSWORD = By.CSS_SELECTOR,'p.woocommerce-LostPassword.lost_password > a'
    INVALID_LOGIN_ERROR = By.CSS_SELECTOR,' div.woocommerce-notices-wrapper > ul'
    INVALID_LOGIN_ERROR_EMAIL = By.CSS_SELECTOR,'div.woocommerce-notices-wrapper > ul > li'
    REGISTER_TITLE = By.CSS_SELECTOR,'div.u-column2.col-2 > h2'
    REGISTER_EMAIL_BLANK = By.ID,'reg_email'
    REGISTER_PASSWORD_BLANK = By.ID,'reg_password'
    REGISTER_BUTTON = By.CSS_SELECTOR,'p:nth-child(5) > button'
    PRIVACY_POLICY = By.LINK_TEXT,'privacy policy'
