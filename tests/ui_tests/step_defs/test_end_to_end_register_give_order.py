from pytest_bdd import then,scenario
from src.ui.pages.checkout_page import CheckOutPage
from src.database.dao.woocommerce_dao.woo_orders_dao import WooOrdersDao

@then('the order should be successfully placed and received')
def verify_order_placed_and_received(order_values,woo_orders_dao:WooOrdersDao):
    order_id = order_values['order_id']
    db_order = woo_orders_dao.get_order_by_order_id(order_id)
    actual_received_message = order_values['order_complete_message']
    expected = "Thank you. Your order has been received."
    assert actual_received_message == expected,(f"Test End to End Register Give Order has failed. "
                                                f"Expected Received Message does not match the Order Received message in UI. "
                                                f"Expected: {expected}, "
                                                f"Actual: {actual_received_message}")

    assert db_order,(f"Test End to End Register Give Order has failed. "
                       f"Unable to find the order in Database. "
                     f"Expected: Order, "
                     f"Actual: {db_order}")

@scenario('tests/ui_tests/features/end_to_end_register_give_order.feature','A newly registered user can successfully place an order with a coupon')
def test_end_to_end_register_give_order():
    pass