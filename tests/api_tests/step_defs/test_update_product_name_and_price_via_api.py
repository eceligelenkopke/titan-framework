from pytest_bdd import when,then,given,scenario
from src.database.dao.woocommerce_dao.woo_products_dao import WooProductsDao
from src.api.helpers.woocommerce_helpers.woo_product_helpers import WooProductHelpers
from src.api.helpers.general_helpers import create_random_string
import random

@when('I update the product price and name',target_fixture="updated_values")
def update_price_and_name_values(woo_product_helpers:WooProductHelpers,product):
    initial_name = product['name']
    initial_price = float(product['regular_price'])
    update = {
        "name":"Updated_PName"+" "+create_random_string(string_length=5),
        "regular_price":str(random.randint(1,999))
    }
    rs_api = woo_product_helpers.update_a_product_via_api(product['id'],**update)
    updated_values = {
        "initial_name":initial_name,
        "initial_price":initial_price,
        "expected_name":update['name'],
        "expected_price":update['regular_price'],
        "updated_name":rs_api['name'],
        "updated_price":rs_api['regular_price']
    }
    return updated_values

@then('Price and Name values should be updated')
def verify_update_values(product,updated_values,woo_products_dao:WooProductsDao):

    initial_api_price = updated_values['initial_price']
    expected_api_price = updated_values['expected_price']
    updated_api_price = updated_values['updated_price']
    updated_db_price = woo_products_dao.get_a_regular_price_by_id(product['id'])
    initial_api_name = updated_values['initial_name']
    expected_api_name = updated_values['expected_name']
    updated_api_name = updated_values['updated_name']
    updated_db_name = woo_products_dao.get_product_from_database_by_id(product['id'])['post_title']

    assert expected_api_price == updated_api_price,(f"Test Update Product Name and Price via API has failed. "
                                                    f"Updated API price does not match the Expected Price. "
                                                    f"Expected: {expected_api_price}, "
                                                    f"Actual: {updated_api_price}")

    assert updated_db_price == updated_api_price,(f"Test Update Product Name and Price via API has failed. "
                                                  f"Updated API price does not match the Updated DB price. "
                                                  f"API Price: {updated_api_price}, "
                                                  f"DB Price: {updated_db_price}")

    assert initial_api_price != updated_api_price,(f"Test Update Product Name and Price via API has failed. "
                                                   f"Initial API price matches Updated API price. Update has failed. "
                                                   f"Initial Price: {initial_api_price}, "
                                                   f"Updated Price: {updated_api_price}")

    assert initial_api_name != updated_api_name,(f"Test Update Product Name and Price via API has failed. "
                                                 f"Initial API name matches Updated API name. Update has failed. "
                                                 f"Initial Name: {initial_api_name}, "
                                                 f"Updated Name: {updated_api_name}")

    assert expected_api_name == updated_api_name,(f"Test Update Product Name and Price via API has failed. "
                                                    f"Updated API name does not match the Expected Name. "
                                                    f"Expected: {expected_api_name}, "
                                                    f"Actual: {updated_api_name}")

    assert updated_api_name == updated_db_name,(f"Test Update Product Name and Price via API has failed. "
                                                f"Updated API name does not match the Updated DB name. "
                                                f"API Name: {updated_api_name}, "
                                                f"DB Name: {updated_db_name}")

@scenario('tests/api_tests/features/update_product_price_and_name_via_api.feature','I should be able to update and price values via API')
def test_update_product_name_and_price_via_api():
    pass