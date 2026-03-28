from pytest_bdd import when,then,scenario
from src.api.helpers.woocommerce_helpers.woo_product_helpers import WooProductHelpers
from src.ui.pages.cart_page import CartPage
from src.ui.pages.checkout_page import CheckOutPage

@when('I proceed to the checkout field')
def proceed_to_checkout(cart_page:CartPage):
    cart_page.click_on_proceed_to_checkout_button()

@when('the product becomes out of stock in the background',target_fixture='updated_product')
def update_product_stock(woo_product_helpers:WooProductHelpers,product):
    update_data = {
        "manage_stock":True,
        "stock_quantity":0
    }
    rs_api = woo_product_helpers.update_a_product_via_api(product['id'],**update_data)
    return rs_api

@when('I attempt to place the order')
def place_the_order(checkout_page:CheckOutPage):
    checkout_page.type_billing_credentials()
    checkout_page.click_on_place_order_button()

@then('the order should be rejected with an out-of-stock error message')
def verify_out_of_stock(checkout_page:CheckOutPage,updated_product,product):
    product_name = updated_product['name']
    out_of_stock_message = checkout_page.get_out_of_stock_message()
    expected_message = f'Sorry, "{product_name}" is not in stock. Please edit your cart and try again. We apologize for any inconvenience caused.'
    initial_quantity = product['stock_quantity']
    updated_quantity = updated_product['stock_quantity']
    assert initial_quantity != updated_quantity,(f"Test Negative Verify Out of Stock Message has failed. "
                                                 f"Initial Stock Value and Updated Stock Value are the same. Update failed. "
                                                 f"Initial Value: {initial_quantity}, "
                                                 f"Updated Value: {updated_quantity}")

    assert expected_message == out_of_stock_message,(f"Test Negative Verify Out of Stock Message has failed. "
                                                     f"Expected Message does not match the message in UI. "
                                                     f"Expected: {expected_message}, "
                                                     f"Actual: {out_of_stock_message}")


@scenario('tests/end_to_end_tests/features/negative_verify_out_of_stock_message.feature','I should be unable to buy an out-of-stock product')
def test_negative_verify_out_of_stock_message():
    pass