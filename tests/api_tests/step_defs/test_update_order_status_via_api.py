from pytest_bdd import when,then,scenario
from src.api.helpers.woocommerce_helpers.woo_order_helpers import WooOrderHelpers


@when('I update the order status',target_fixture="status")
def update_order_status(order,woo_order_helpers:WooOrderHelpers):
    update_data = {
        "status":"cancelled"
    }
    rs_api = woo_order_helpers.update_an_order_via_api(order['id'],**update_data)
    api_status = rs_api['status']
    status_values = {
        "expected":update_data['status'],
        "actual":api_status,
        "response":rs_api
    }
    return status_values
@then('The Order status should be updated')
def verify_order_status_updated(order,status):
    initial = order['status']
    expected = status['expected']
    actual = status['actual']
    assert initial != actual,(f"Test Update and Verify Order Status via API has failed. "
                                             f"Initial Order Status matches the Updated Order Status. "
                                             f"Initial Status: {initial}, "
                                             f"Updated Status: {actual}")
    assert expected == actual,(f"Test Update and Verify Order Status via API has failed. "
                               f"Expected Order Status does not match the Actual Order Status. "
                               f"Expected: {expected}, "
                               f"Actual: {actual}")


@then('The Order should have the expected product')
def verify_product_id_matches(product,status):
    response = status['response']
    order_product_id = response['line_items'][0]['product_id']
    product_id = product['id']
    assert order_product_id == product_id,(f"Test Update and Verify Order Status via API has failed. "
                                          f"Product ID in Order does not match the Expected Product ID. "
                                          f"Expected: {product_id}, "
                                          f"Actual: {order_product_id}")


@scenario('tests/api_tests/features/update_order_status_via_api.feature','I should be able to update order status via API')
def test_update_order_status_via_api():
    pass