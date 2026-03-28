from pytest_bdd import when,then,scenario
from src.ui.pages.cart_page import CartPage

@when('I remove the product from the cart')
def remove_product_from_cart(cart_page:CartPage):
    cart_page.remove_product_from_cart()

@then('the cart should display a product removed confirmation message')
def verify_remove_message(cart_page:CartPage,product):
    expected = f'“{product['name']}” removed. Undo?'
    actual_message = cart_page.get_product_remove_message()
    assert expected == actual_message,(f"Test Add to Cart Remove Verify Product Removed Has Failed. "
                                       f"Expected Removed Message does not match the Actual Removed Message. "
                                       f"Expected: {expected}, "
                                       f"Actual: {actual_message}")
@then('the cart should be completely empty')
def verify_cart_empty(cart_page:CartPage):
    expected = "Your cart is currently empty."
    actual_message = cart_page.get_cart_empty_message()
    assert expected == actual_message,(f"Test Add to Cart Remove Verify Product Removed has failed. "
                                       f"Expected Cart Empty message does not match the Message in UI. "
                                       f"Expected: {expected}, "
                                       f"Actual: {actual_message}")
@scenario('tests/ui_tests/features/add_to_cart_remove_verify_product_removed.feature','A user can successfully remove an item from their cart')
def test_add_to_cart_remove_verify_product_removed():
    pass