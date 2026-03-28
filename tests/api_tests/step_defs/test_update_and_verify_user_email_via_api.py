from pytest_bdd import when,then,scenario
from src.api.helpers.woocommerce_helpers.woo_customer_helpers import WooCustomerHelpers
from src.api.helpers.general_helpers import generate_random_email

from src.database.dao.woocommerce_dao.woo_customers_dao import WooCustomersDao


@when('I update the customer email',target_fixture='email_values')
def update_the_email_value(woo_customer_helpers:WooCustomerHelpers,customer):
    initial_email = customer['email']
    new_email = {
        "email":generate_random_email()
    }
    rs_api = woo_customer_helpers.update_customer_from_api(customer['id'],**new_email)
    updated_email = rs_api['email']
    email_values = {
        "new_email":new_email['email'],
        "first_email":initial_email,
        "updated_email":updated_email
    }
    return email_values

@then('Updated email should be different than the Initial email')
def verify_email_changed_correctly(email_values):
    first_email = email_values['first_email']
    updated_email = email_values['updated_email']
    assert first_email != updated_email, (f"Test Update and Verify user Email via API has failed. "
                                          f"Unable to update the email value. First and Updated email values are a match. "
                                          f"First Email: {first_email}, "
                                          f"Actual: {updated_email}")

@then('And the customer details should reflect the new email')
def verify_email_updated_correctly(email_values,customer,woo_customers_dao:WooCustomersDao):
    new_email = email_values['new_email']
    updated_email = email_values['updated_email']
    email_in_db = woo_customers_dao.get_a_customer_by_id(customer['id'])['user_email']
    assert new_email == updated_email,(f"Test Update and Verify user Email via API has failed. "
                                       f"Email Sent to Update does not match the Updated Email Value."
                                       f"Expected: {new_email}, "
                                       f"Actual : {updated_email}")

    assert email_in_db == updated_email, (f"Test Update and Verify user Email via API has failed. "
                                          f"Email in DB does not match the Updated email in API. "
                                          f"Email in DB: {email_in_db}, "
                                          f"Email in API: {updated_email} ")

@scenario('tests/api_tests/features/update_and_verify_user_email_via_api.feature','I should be able to update user email via API')
def test_update_and_verify_user_email_via_api():
    pass