from pytest_bdd import when,then,scenario
from src.ui.pages.cart_page import CartPage
from src.api.helpers.general_helpers import create_random_string

@when('I try to apply an invalid coupon',target_fixture='coupon')
def apply_invalid_coupon(cart_page:CartPage):
    coupon = create_random_string(string_length=5).lower()
    cart_page.type_a_coupon(coupon)
    cart_page.click_on_apply_coupon()
    return coupon

@then('I should verify invalid coupon message')
def verify_invalid_coupon_message(coupon,cart_page:CartPage):
    expected = f'Coupon "{coupon}" cannot be applied because it does not exist.'
    actual = cart_page.get_invalid_coupon_message()
    assert expected == actual, (f"Test Verify Invalid Coupon Message has failed. "
                                f"Expected Invalid Coupon Message does not match the Actual Coupon Invalid Message. "
                                f"Expected:{expected}, "
                                f"Actual: {actual}")

@scenario('tests/ui_tests/features/negative_verify_invalid_coupon_message.feature','I should be unable to apply an invalid coupon')
def test_verify_invalid_coupon_message():
    pass