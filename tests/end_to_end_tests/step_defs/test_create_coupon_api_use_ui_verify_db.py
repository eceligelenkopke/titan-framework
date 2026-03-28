from pytest_bdd import then,scenario
from src.database.dao.woocommerce_dao.woo_orders_dao import WooOrdersDao

@then('Coupon should be applied successfully')
def verify_coupon_applied(ui_prices,user_values,woo_orders_dao:WooOrdersDao,order_values):
    initial_ui_price = ui_prices['initial']
    order_id = order_values['order_id']
    expected_email = user_values['email']
    db_order = woo_orders_dao.get_order_by_order_id(order_id)
    db_order_id = db_order['id']
    db_email = db_order['billing_email']

    db_price = float(db_order['total_amount'])
    updated_price = ui_prices['updated']

    assert db_email == expected_email,(f"Test Create Coupon via API use UI verify DB has failed. "
                                       f"Email in Database does not match the Expected Email. "
                                       f"Expected Email: {expected_email}, "
                                       f"Email in DB: {db_email} ")
    assert db_order_id == order_id,(f"Test Create Coupon via API use UI verify DB has failed. "
                                    f"UI Order ID does not match the DB Order ID. "
                                    f"UI ID: {order_id}, "
                                    f"DB ID: {db_order_id}")
    assert db_price == updated_price,(f"Test Create Coupon via API use UI verify DB has failed. "
                                      f"Coupon Applied Price in UI does not match the Coupon Applied Price in Database. "
                                      f"UI Price: {updated_price}, "
                                      f"DB Price: {db_price}")

    assert initial_ui_price != updated_price,(f"Test Create Coupon via API use UI verify DB has failed. "
                                              f"Initial UI price matches the Updated UI Price. Coupon is not applied. "
                                              f"Initial Price: {initial_ui_price}, "
                                              f"Updated Price: {updated_price}")


@scenario('tests/end_to_end_tests/features/create_coupon_api_use_ui_verify_db.feature','I create a coupon via API, apply via UI and verify via DB')
def test_create_coupon_api_use_ui_verify_db():
    pass
