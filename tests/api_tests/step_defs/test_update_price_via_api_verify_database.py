import random
from pytest_bdd import when,given,then,scenario
from src.api.helpers.woocommerce_helpers.woo_product_helpers import WooProductHelpers
from src.database.dao.woocommerce_dao.woo_products_dao import WooProductsDao

@when('I update the price values',target_fixture="prices")
def update_price_values_with_api(woo_product_helpers:WooProductHelpers,woo_products_dao:WooProductsDao, product):
    db_initial = woo_products_dao.get_a_regular_price_by_id(product['id'])
    api_initial = product['regular_price']
    new_price = {
        "regular_price":str(random.randint(1,999))
    }
    rs_api = woo_product_helpers.update_a_product_via_api(product['id'],**new_price)
    price_values = {
       "updated": rs_api['regular_price'],
        "db_initial":db_initial,
        "api_initial":api_initial
    }
    return price_values

@then('the initial price values should match')
def verify_first_prices_match(prices):
    api_initial = prices['api_initial']
    db_initial = prices['db_initial']
    assert api_initial == db_initial,(f"Test Update Price Value via API verify Database has failed. "
                                      f"Initial Price in API does not match the Initial Price in Database. "
                                      f"API Initial: {api_initial}, "
                                      f"DB Initial: {db_initial}")

@then('the price should be updated correctly in database')
def verify_db_update(product,prices,woo_products_dao:WooProductsDao):
    api_updated = prices['updated']
    db_initial = prices['db_initial']
    db_updated = woo_products_dao.get_a_regular_price_by_id(product['id'])
    assert db_initial != db_updated,(f"Test Update Price Value via API verify Database has failed. "
                                     f"Initial Price in Database matches the Updated Price in Database. "
                                     f"DB Initial: {db_initial}, "
                                     f"DB Updated: {db_updated}")

    assert api_updated == db_updated,(f"Test Update Price Value via API verify Database has failed. "
                                      f"Updated Price in API does not match the Updated Price in DB. "
                                      f"API Updated: {api_updated}, "
                                      f"DB Updated: {db_updated}")


@scenario('tests/api_tests/features/update_price_via_api_verify_database.feature',"Update a random product's regular price and verify data consistency across API and DB")
def test_verify_update_price_api_verify_db():
    pass