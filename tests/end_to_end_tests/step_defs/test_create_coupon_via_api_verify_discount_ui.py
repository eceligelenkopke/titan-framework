from pytest_bdd import then,scenario

@then('The total price should be reduced by the coupon amount')
def verify_coupon_applied(coupon, ui_prices):
    initial = ui_prices['initial']
    updated = ui_prices['updated']
    coupon_amount = float(coupon['amount'])
    
    expected_price = max(0.0, initial - coupon_amount)
    
    assert updated == expected_price, (f"Test Create Coupon via API verify Discount in UI has failed. "
                                       f"Expected updated price: {expected_price}, "
                                       f"Actual updated price: {updated}, "
                                       f"Initial Price: {initial}, "
                                       f"Coupon Amount: {coupon_amount}")

@scenario('tests/end_to_end_tests/features/create_coupon_via_api_verify_discount_ui.feature','I should be able to apply coupon after creating in API')
def test_create_coupon_via_api_verify_discount_ui():
    pass