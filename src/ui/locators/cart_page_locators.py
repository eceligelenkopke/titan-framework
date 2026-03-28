from selenium.webdriver.common.by import By
class CartPageLocators:
    COUPON_LINE = By.ID,'coupon_code'
    APPLY_COUPON_BUTTON = By.CSS_SELECTOR,'tr:nth-child(2) > td > div > button'
    COUPON_APPLIED_MESSAGE = By.CSS_SELECTOR,'div.woocommerce-notices-wrapper > div'
    PROCEED_TO_CHECKOUT_BUTTON = By.CSS_SELECTOR,'a.checkout-button.button.alt.wc-forward'
    BLOCK_UI_LAYER = By.CSS_SELECTOR,'div.blockUI.blockOverlay'
    PRICE_VALUE = By.CSS_SELECTOR,'td.product-price > span > bdi'
    TOTAL_PRICE = By.CSS_SELECTOR,'tr.order-total > td > strong > span > bdi'
    QUANTITY_LINE = By.CSS_SELECTOR,"input[type='number'].qty"
    UPDATE_CART_BUTTON = By.CSS_SELECTOR,'tr:nth-child(2) > td > button'
    CART_UPDATED_MESSAGE = By.CSS_SELECTOR,'div.woocommerce-message'
    PRODUCT_REMOVED_MESSAGE = By.CSS_SELECTOR,'div.woocommerce-message'
    CART_EMPTY_MESSAGE = By.CSS_SELECTOR,'div.cart-empty.woocommerce-info'
    REMOVE_ITEM_BUTTON = By.CSS_SELECTOR,'a.remove'
    CART_PAGE_PRODUCT_NAME = By.CSS_SELECTOR,'td.product-name > a'
    INVALID_COUPON_MESSAGE = By.ID,'coupon-error-notice'
    COUPON_LIMIT_MESSAGE = By.ID,'coupon-error-notice'

