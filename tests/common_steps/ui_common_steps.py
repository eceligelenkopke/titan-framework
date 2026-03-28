import pytest
from pytest_bdd import when,given,parsers
from src.ui.pages.home_page import HomePage
from src.ui.pages.my_account_signed_out import MyAccountSignedOutPage
from src.ui.pages.my_account_signed_in import MyAccountSignedInPage
from src.ui.pages.cart_page import CartPage
from src.ui.pages.product_page import ProductPage
from src.ui.pages.checkout_page import CheckOutPage
from src.api.helpers.general_helpers import generate_random_email,generate_random_password
from src.database.dao.woocommerce_dao.woo_customers_dao import WooCustomersDao

@pytest.fixture()
def product_page():
    return ProductPage()
@pytest.fixture()
def my_acc_signed_out_page():
    return MyAccountSignedOutPage()
@pytest.fixture()
def my_acc_signed_in_page():
    return MyAccountSignedInPage()
@pytest.fixture()
def cart_page():
    return CartPage()
@pytest.fixture()
def checkout_page():
    return CheckOutPage()
@pytest.fixture()
def home_page():
    return HomePage()

@given(parsers.parse('I navigate to the {page_name}'))
@when(parsers.parse('I navigate to the {page_name}'))
def navigate_to_pages(page_name,cart_page:CartPage,home_page:HomePage,my_acc_signed_out_page:MyAccountSignedOutPage):
    page_name = page_name.lower()
    if page_name == "cart page":
        cart_page.go_to_cart_page()

    elif page_name == "home page":
        home_page.go_to_home_page()

    elif page_name == "my account signed out page":
        my_acc_signed_out_page.go_to_my_acc_signed_out_page()

@given('I navigate to product page')
@when('I navigate to product page')
def navigate_to_product_page(product_page:ProductPage,product):
    product_page.go_to_product_page_by_slug(product['slug'])

@when('I get the product details from the product page',target_fixture='ui_product_values')
def get_product_details(product_page:ProductPage):
    ui_name = product_page.product_title_in_product_page().lower()
    ui_price = product_page.get_product_page_price()
    ui_product_values = {
        "name": ui_name,
        "price": ui_price
    }
    return ui_product_values

@when('I add the product to cart',target_fixture='added_to_cart_message')
def add_product_to_cart(product_page:ProductPage):
    product_page.click_on_add_to_cart_button()
    product_page.wait_until_added_to_cart_message()
    success_message = product_page.get_added_to_cart_message()
    product_page.click_on_view_cart_button()
    return success_message
@given('I register with valid email and password',target_fixture='user_values')
@when('I register with valid email and password',target_fixture='user_values')
def register_new_account_global(resource_registry, woo_customers_dao:WooCustomersDao, my_acc_signed_out_page:MyAccountSignedOutPage):
    email = generate_random_email()
    password = generate_random_password()
    my_acc_signed_out_page.go_to_my_acc_signed_out_page()
    my_acc_signed_out_page.type_register_email(email)
    my_acc_signed_out_page.type_register_password(password)
    my_acc_signed_out_page.scroll_until_register_button_visible()
    my_acc_signed_out_page.click_on_register_button()
    customer = woo_customers_dao.get_a_customer_by_email(email)
    resource_registry['customer'].append(customer['ID'])
    values = {
        "email":email,
        "password":password
    }
    return values
@when('I apply the coupon',target_fixture="ui_prices")
def apply_coupon_global(coupon,cart_page:CartPage):
    cart_page.type_a_coupon(coupon['code'])
    cart_page.click_on_apply_coupon()
    cart_page.wait_until_coupon_applied()
    initial_price = cart_page.get_product_price_from_ui()
    updated_price = cart_page.get_final_price_value_via_ui()
    price_values = {
        "initial":initial_price,
        "updated":updated_price
    }
    return price_values

@when('I make the order',target_fixture='order_values')
def make_the_order_global(cart_page:CartPage,resource_registry, checkout_page:CheckOutPage):
    cart_page.click_on_proceed_to_checkout_button()
    checkout_page.type_billing_credentials()
    checkout_page.click_on_place_order_button()
    order_message = checkout_page.get_order_received_message()
    order_id = checkout_page.get_order_number()
    order_price = checkout_page.get_checkout_order_price()
    resource_registry['order'].append(order_id)
    order_values = {
        "order_complete_message":order_message,
        "order_id":order_id,
        "order_price":order_price
    }

    return order_values
