from pytest_bdd import then,scenario
from src.database.dao.woocommerce_dao.woo_products_dao import WooProductsDao

@then('the product details in the database should match the created product')
def verify_details_match(product,woo_products_dao:WooProductsDao):
    api_id = product['id']
    api_name = product['name']
    db_product = woo_products_dao.get_product_from_database_by_id(api_id)
    db_id = db_product['ID']
    db_name = db_product['post_title']

    assert api_id == db_id,(f"Test Verify Created Product via API exists in Database has failed."
                                                        f"ID coming from API and ID in Database do not match."
                                                        f"ID in API: {api_id}, "
                                                        f"ID in DB: {db_id}")

    assert api_name == db_name,(f"Test Verify Created Product via API exists in  Database has failed."
                                                                f"Product Name coming from API and Product Name coming from Database do not match."
                                                                f"Product Name in API: {api_name}, "
                                                                f"Product Name in DB: {db_name}")


@scenario('tests/api_tests/features/create_and_verify_product_in_db.feature','Create a random product via API and verify in Database')
def test_verify_created_product_exists_in_database():
    pass