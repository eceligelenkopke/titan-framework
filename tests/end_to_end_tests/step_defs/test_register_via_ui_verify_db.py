from pytest_bdd import then,scenario
from src.database.dao.woocommerce_dao.woo_customers_dao import WooCustomersDao

@then('the user account should be successfully created in the database',target_fixture='db_customer')
def verify_user_created_in_db(user_values,woo_customers_dao:WooCustomersDao):
    email = user_values['email']
    db_customer = woo_customers_dao.get_a_customer_by_email(email)
    db_email = db_customer['user_email']
    assert email == db_email,(f"Test Register with UI and Verify User existed in DB has failed. "
                                 f"Unable to reach the email value in Database. "
                                 f"Expected: {email}, "
                                 f"Actual: {db_email}")
    return db_customer


@then("the user password must be stored securely as encrypted data")
def verify_password_encrypted(user_values,db_customer):
    password = user_values['password']
    assert password not in db_customer['user_pass'],(f"Test Register with UI and Verify User existed in DB has failed. "
                                        f"Able to reach the password value from database. Security LEAK DETECTED. "
                                        f"Expected: encrypted data, "
                                        f"Actual: {db_customer}")




@scenario('tests/end_to_end_tests/features/register_via_ui_verify_db.feature',"A newly registered user's credentials should be securely stored in the database")
def test_register_with_selenium_verify_db():
    pass