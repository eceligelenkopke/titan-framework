from pytest_bdd import then,scenario
from src.api.helpers.woocommerce_helpers.woo_order_helpers import WooOrderHelpers
from src.database.dao.woocommerce_dao.woo_orders_dao import WooOrdersDao

@then('Total Price with Coupon cannot be negative')
def verify_total_price(woo_order_helpers:WooOrderHelpers,woo_orders_dao:WooOrdersDao,ui_prices,order_values):
    order_id = order_values['order_id']
    api_order = woo_order_helpers.get_an_order_by_order_id(order_id)
    final_price_ui = ui_prices['updated']
    db_price = woo_orders_dao.get_total_amount_by_order_id(order_id)
    api_price = float(api_order['total'])
    assert final_price_ui == db_price, (f"Test Negative Higher Coupon Amount than Cart has failed. "
                                  f"Order Price in UI does not match the Price in Database."
                                  f"UI Price: {final_price_ui}, "
                                  f"DB Price: {db_price} ")

    assert db_price == api_price,(f"Test Negative Higher Coupon Amount than Cart has failed. "
                                  f"Order Price in API does not match the Price in Database. "
                                  f"Price in API: {api_price}, "
                                  f"Price in DB: {db_price}")

    assert api_price >=0 and db_price>=0 and final_price_ui>=0,(f"Test Negative Higher Coupon Amount than Cart has failed. "
                                                          f"Price Value is negative in one of the API,UI,DB layers. "
                                                          f"Price in UI: {final_price_ui}, "
                                                          f"Price in DB: {db_price}, "
                                                          f"Price in API: {api_price}")
@scenario('tests/end_to_end_tests/features/negative_higher_coupon_amount_than_cart.feature','Total Price can not be negative')
def test_negative_higher_coupon_amount_than_cart():
    pass