from pytest_bdd import then,scenario
from src.database.dao.woocommerce_dao.woo_orders_dao import WooOrdersDao

@then('the order details should be recorded correctly in the database')
def verify_order_elements_in_db(order_values,woo_orders_dao:WooOrdersDao,user_values):
    order_id = order_values['order_id']
    db_order = woo_orders_dao.get_order_by_order_id(order_id)
    db_email = db_order['billing_email']
    user_email = user_values['email']
    assert db_email == user_email,(f"Test Create a Product via API buy in UI and verify Order in DB has failed. "
                                   f"Email in Database does not match the Email in UI. "
                                   f"Email in UI: {user_email}, "
                                   f"Email in DB: {db_email}")
    db_price = float(db_order['total_amount'])
    ui_price = float(order_values['order_price'])

    assert db_price == ui_price,(f"Test Create a Product via API buy in UI and verify Order in DB has failed. "
                                 f"Price in UI does not match the Price in Database. "
                                 f"Price in UI: {ui_price}, "
                                 f"Price in DB: {db_price}")

@scenario('tests/end_to_end_tests/features/create_product_api_buy_ui_verify_order_db.feature','Create product via API, buy it via UI, and verify order via DB')
def test_create_product_api_buy_ui_verify_order_db():
    pass
