from pytest_bdd import when,then,given,scenario
from src.database.dao.woocommerce_dao.woo_products_dao import WooProductsDao
from src.api.helpers.woocommerce_helpers.woo_product_helpers import WooProductHelpers


@when('I delete the product')
def delete_the_product_via_api(product, woo_product_helpers:WooProductHelpers):
    woo_product_helpers.delete_a_product_by_id_via_api(product['id'], expected_status_code=200)

@then('The Product should be deleted')
def verify_product_unable_to_reach(product,woo_product_helpers:WooProductHelpers,woo_products_dao:WooProductsDao):
    rs_api = woo_product_helpers.get_a_product_by_id_via_api(product['id'],expected_status_code=404)
    expected_api_message = 'Invalid ID.'
    actual_api_message = rs_api['message']
    product_in_db = woo_products_dao.get_product_from_database_by_id(product['id'])

    assert actual_api_message == expected_api_message, (f"Test Delete and Verify Product Deleted via API has failed."
                        f"The Message coming from API does not match the expected API message. "
                                                       f"Expected: {expected_api_message}, "
                                                       f"Actual: {actual_api_message}")

    assert product_in_db is None, (f"Test Delete and Verify Product Deleted via API has failed."
                                       f"Getting Product in Database should return none after deleting but it returns data. "
                                       f"Data Reached: {product_in_db}")




@scenario('tests/api_tests/features/delete_and_verify_product_deleted_via_api.feature','I should delete a product and verify it is deleted')
def test_delete_and_verify_product_deleted_via_api():
    pass