from selenium.webdriver.common.by import By

class HomePageLocators:

    ACCOUNT_BTN = By.CSS_SELECTOR,'.right-box > span > a'
    SEARCH_BTN = By.CSS_SELECTOR,'form > button'
    SEARCH_FIELD = By.ID,'woocommerce-product-search-field-0'
    SEARCH_FIELD_CATEGORIES = By.CSS_SELECTOR,'div.col-lg-5.col-md-7.col-sm-7.col-12.align-self-center.product-search.text-end > div > button'
    MY_CART_BTN = By.CSS_SELECTOR,'div.cart-text-count > span'
    CATEGORIES_BTN_LEFT = By.CSS_SELECTOR,'div.col-lg-3.col-md-6.col-sm-7.logo-box.align-self-center > div > button'
    CATEGORIES_BTN_LEFT_2 = By.CSS_SELECTOR,'div.col-lg-3.col-md-6.col-sm-7.logo-box.align-self-center > div > button > span'
    NEWSLETTER_SIGN_UP_INPUT_BLANK = By.ID,'srfm-email-03e2a21a-lbl-WW91ciBFbWFpbCBQbGVhc2U'
    NEWSLETTER_SUCCESS_MESSAGE = By.CSS_SELECTOR,'#srfm-success-message-page-3084 > p:nth-child(3)'
    ADD_TO_CART_BTN = By.CSS_SELECTOR,'a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart'
    PRODUCT_TITLE = By.CSS_SELECTOR,'woocommerce-loop-product__title'
    PRODUCT_IMAGE = By.CSS_SELECTOR,'a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > img'
    PRODUCT_PRICE = By.CSS_SELECTOR,'a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > span > span > bdi'
    VIEW_CART_BUTTON = By.CSS_SELECTOR,'a.added_to_cart.wc-forward'
    CART_VALUE = By.CSS_SELECTOR,'span > a > div.icon > span'
    WEBSITE_TITLE = By.CSS_SELECTOR,'div.col-lg-3.col-md-5.col-sm-5.col-12.align-self-center > div > p > a'
    PRODUCT_SELECTOR = By.CSS_SELECTOR,'.product_cat-uncategorized.shipping-taxable.purchasable.product-type-simple'

    NEW_ARRIVALS_TOP_BAR = By.ID, 'menu-item-1022'
    COLLECTIONS_TOP_BAR = By.ID, 'menu-item-1023'
    SHOP_BY_CATEGORY_TOP_BAR = By.ID,'menu-item-1024'

    ABOUT_ME_BUTTON_SIDE_BAR = By.ID,'menu-item-1017'


    SEARCH_RESULTS_BAR = By.CSS_SELECTOR,'h1.woocommerce-products-header__title.page-title'
    NO_PRODUCT_FOUND_MESSAGE = By.CSS_SELECTOR,'div.woocommerce-info'