from pytest_bdd import when,then,scenario
from src.ui.pages.cart_page import CartPage

@when('I increase the product quantity',target_fixture='expected_quantity')
def update_product_quantity(cart_page:CartPage):
    expected_quantity = 5
    cart_page.delete_existing_quantity_value()
    cart_page.update_quantity_value(quantity_value=expected_quantity)
    return expected_quantity

@then('the cart total price should update to reflect the new quantity')
def verify_price_updated(cart_page:CartPage,expected_quantity,ui_product_values):
    updated_quantity = cart_page.get_existing_quantity_value()
    initial_price = ui_product_values['price']
    updated_price = cart_page.get_final_price_value_via_ui()
    assert expected_quantity == updated_quantity,(f"Test Verify Quantity and Price Updated Correctly has failed. "
                                             f"Expected Quantity value does not match the Updated Quantity Value in UI. "
                                             f"Expected: {expected_quantity}, "
                                             f"Actual: {updated_quantity}")

    assert initial_price * updated_quantity == updated_price,(f"Test Verify Quantity and Price Updated Correctly has failed. "
                                                              f"Updated Price in UI has been miscalculated. "
                                                              f"Initial Price: {initial_price} * Updated Quantity Value: {updated_quantity}  = {initial_price * updated_quantity} "
                                                              f"Updated Price: {updated_price}")



@scenario('tests/ui_tests/features/verify_quantity_and_price_updated_correctly.feature','Cart total updates dynamically when product quantity is increased')
def test_verify_quantity_price_updated_correctly():
    pass