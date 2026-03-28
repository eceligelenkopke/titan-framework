from pytest_bdd import then,scenario
from src.database.dao.woocommerce_dao.woo_orders_dao import WooOrdersDao


@then('Order details should match details in database')
def verify_order_id_api_match_id_in_db(order,woo_orders_dao:WooOrdersDao):
    api_email = order['billing']['email']
    api_id = order['id']

    order_db = woo_orders_dao.get_order_by_order_id(api_id)
    db_id = order_db['id']
    db_email = order_db['billing_email']
    assert api_id == db_id, (f"Test Create Order via API verify exists in Database has failed. "
                            f"ID in api does not match the ID in Database. "
                            f"ID in API: {api_id}, "
                            f"ID in DB: {db_id}")


    assert api_email == db_email, (f"Test Create Order via API verify exists in Database has failed. "
                                   f"Email in API does not match the Email in Database. "
                                   f"Email in API: {api_email}, "
                                   f"Email in DB: {db_email}")

@scenario('tests/api_tests/features/create_order_via_api_verify_db.feature','I should create order via api and verify it exists in database')
def test_create_order_via_api_verify_db():
   pass