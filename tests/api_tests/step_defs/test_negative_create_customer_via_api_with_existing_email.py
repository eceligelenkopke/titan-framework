from pytest_bdd import when,then,given,scenario
from src.api.helpers.woocommerce_helpers.woo_customer_helpers import WooCustomerHelpers

@given('I get the existing user email',target_fixture='existing_email')
def get_existing_user_email(customer):
    return customer['email']

@when('I try to register with existing user email',target_fixture='api_response')
def register_with_existing_email(existing_email,woo_customer_helpers:WooCustomerHelpers):
    update_values = {
        "email":existing_email
    }
    rs_api = woo_customer_helpers.create_customer_in_api(**update_values,expected_status_code=400)
    return rs_api

@then('The user should not be registered')
def verify_register_failed(api_response,existing_email):
    api_message = api_response['message']
    expected_message = f"An account is already registered with {existing_email}. Please log in or use a different email address."
    assert api_message == expected_message,(f"Test Negative Register via API with existing email has failed."
                                            f"API Response message does not match the expected error message. "
                                             f"Expected: {expected_message}, "
                                             f"Actual: {api_message}")

@scenario('tests/api_tests/features/negative_create_customer_via_api_with_existing_email.feature','I should not be able to register with an existing email')
def test_negative_register_via_api_with_existing_email():
    pass