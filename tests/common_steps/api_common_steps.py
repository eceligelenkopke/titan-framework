from pytest_bdd import when,given,parsers
from src.api.helpers.woocommerce_helpers.woo_product_helpers import WooProductHelpers
from src.api.helpers.woocommerce_helpers.woo_coupon_helpers import WooCouponHelpers
from src.api.helpers.woocommerce_helpers.woo_customer_helpers import WooCustomerHelpers
from src.api.helpers.woocommerce_helpers.woo_order_helpers import WooOrderHelpers


def get_product_kwargs(special_condition):
    payload = {}
    if special_condition == 'with one stock':
        payload = {
            "stock_quantity": 1,
            "manage_stock": True
        }
    elif special_condition == "out of stock":
        payload = {
            "stock_quantity": 0,
            "manage_stock": True
        }
    elif special_condition == "whose price is 30$":
        payload = {
            "regular_price":"30"
        }
    return payload
def get_coupon_kwargs(special_condition):
    special_condition = special_condition.lower()
    payload = {}
    if special_condition == "fixed-cart":
        payload = {
            "discount_type":"fixed_cart"
        }
    elif special_condition == "one usage limit":
        payload = {
            "usage_limit":1
        }
    elif special_condition == "whose value exceeds the product price":
        payload = {
            "discount_type":"fixed_cart",
            "amount":"50"
        }
    return payload

@when('I have a product',target_fixture='product')
@given('I have a product',target_fixture='product')
@when('I create a product',target_fixture='product')
@given('I create a product',target_fixture='product')
def create_product_api_raw(woo_product_helpers:WooProductHelpers,resource_registry):
    product = woo_product_helpers.create_a_product_in_api()
    resource_registry['product'].append(product['id'])
    return product

@when(parsers.parse('I create a product {special_condition}'),target_fixture='product')
@given(parsers.parse('I have a product {special_condition}'),target_fixture='product')
def create_product_api_condition(woo_product_helpers:WooProductHelpers,resource_registry,special_condition):
    kwargs = get_product_kwargs(special_condition)
    product = woo_product_helpers.create_a_product_in_api(**kwargs)
    resource_registry['product'].append(product['id'])
    return product

@given('I have a coupon',target_fixture='coupon')
def create_a_coupon_raw(woo_coupon_helpers:WooCouponHelpers,resource_registry):
    coupon = woo_coupon_helpers.create_a_coupon()
    resource_registry['coupon'].append(coupon['id'])
    return coupon

@given(parsers.parse('I have a {special_condition} discount coupon'),target_fixture='coupon')
def create_a_coupon_condition(woo_coupon_helpers:WooCouponHelpers,resource_registry,special_condition):
    kwargs = get_coupon_kwargs(special_condition)
    coupon = woo_coupon_helpers.create_a_coupon(**kwargs)
    resource_registry['coupon'].append(coupon['id'])
    return coupon


@given('I have a customer',target_fixture='customer')
@given('I create a customer',target_fixture='customer')
@when('I create a customer',target_fixture='customer')
def create_a_customer_global(woo_customer_helpers:WooCustomerHelpers,resource_registry):
    customer = woo_customer_helpers.create_customer_in_api()
    resource_registry['customer'].append(customer['id'])
    return customer

@given('I make an order via API',target_fixture='order')
@when('I make an order via API',target_fixture="order")
def make_order_via_api(woo_order_helpers:WooOrderHelpers,resource_registry,product):
    order = woo_order_helpers.create_an_order_via_api(product['id'])
    resource_registry['order'].append(order['id'])
    return order

