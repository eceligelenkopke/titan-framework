from pytest_bdd import when,then,scenario
from src.ui.pages.cart_page import CartPage

@when('I attempt to apply the coupon again')
def apply_coupon_again(cart_page:CartPage,coupon):
    cart_page.type_a_coupon(coupon['code'])
    cart_page.click_on_apply_coupon()

@then('the system must reject the coupon with a usage limit error message')
def verify_unusable_limit_error(cart_page:CartPage,coupon):
    expected_message = f'Usage limit for coupon "{coupon['code']}" has been reached. Please try again after some time, or contact us for help.'
    actual_message = cart_page.get_coupon_usage_limit_message()

    assert expected_message == actual_message,(f"Test Negative Verify Coupon Usage limit message has failed. "
                                               f"Coupon Limit Message in UI does not match the Expected Coupon Limit Message. "
                                               f"Expected: {expected_message}, "
                                               f"Actual: {actual_message}")

@scenario('tests/end_to_end_tests/features/negative_coupon_usage_limit.feature','A single-use coupon cannot be applied a second time after being consumed')
def test_negative_coupon_usage_limit():
    pass