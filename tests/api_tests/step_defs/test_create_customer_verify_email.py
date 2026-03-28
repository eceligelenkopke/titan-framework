from pytest_bdd import then,scenario

@then('the returned user data should contain a valid email')
def verify_email_exists(customer):

    assert customer['email'],(f"Test Create Customer Verify Email exists has failed."
                           f"Unable to reach the customer email in API. "
                           f"Expected: customer_email, "
                           f"Actual : {customer['email']}")


@scenario('tests/api_tests/features/create_customer_verify_email.feature','Create a new user via API and verify email existence')
def test_create_customer_api_verify_email():
    pass