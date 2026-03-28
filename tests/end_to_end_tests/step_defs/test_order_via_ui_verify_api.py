from pytest_bdd import then,scenario
from src.api.helpers.woocommerce_helpers.woo_order_helpers import WooOrderHelpers

@then('the order should be successfully created in the system with the matching checkout price')
def verify_order_created(order_values, woo_order_helpers:WooOrderHelpers):
    order_id = order_values['order_id']
    ui_price = order_values['order_price']
    rs_api = woo_order_helpers.get_an_order_by_order_id(order_id)
    api_price = float(rs_api['total'])

    assert ui_price == api_price,(f"Test Order via UI verify API has failed. "
                                  f"Order Price in UI does not match the Order Price in API. "
                                  f"Price in UI: {ui_price}, "
                                  f"Price in API: {api_price}")


@scenario('tests/end_to_end_tests/features/order_via_ui_verify_api.feature','A completed UI order should be correctly recorded in the system backend')
def test_order_via_ui_verify_api():
    pass