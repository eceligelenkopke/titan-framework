from pytest_bdd import then,scenario

@then('The total price should be reduced by the coupon amount')
def verify_coupon_applied(coupon,ui_prices):
    initial = ui_prices['initial']
    updated = ui_prices['updated']
    coupon_amount = float(coupon['amount'])
    assert updated + coupon_amount == initial, (f"Test Create Coupon via API verify Discount in UI has failed. "
                                                            f"Updated Price added to Coupon Discount Amount does not match the Initial Price. "
                                                            f"Updated Price: {updated} + Coupon Amount: {coupon_amount} = Total: {updated+coupon_amount}, "
                                                            f"Initial Price: {initial}, "
                                                            f"Difference: {initial - (updated + coupon_amount)}")

@scenario('tests/end_to_end_tests/features/create_coupon_via_api_verify_discount_ui.feature','I should be able to apply coupon after creating in API')
def test_create_coupon_via_api_verify_discount_ui():
    pass