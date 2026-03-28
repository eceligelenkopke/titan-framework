from pytest_bdd import when,then,scenario,parsers
from src.api.helpers.general_helpers import generate_random_email,generate_random_password,create_random_string
from src.ui.pages.my_account_signed_out import MyAccountSignedOutPage

@when(parsers.parse('I attempt to login with an unregistered "{credential_type}"'),target_fixture='login_value')
def login_with_invalid_credentials(my_acc_signed_out_page:MyAccountSignedOutPage,credential_type):
    login_value = ""
    password = generate_random_password()
    if credential_type == "email":
        login_value = generate_random_email()
    elif credential_type == "username":
        login_value = create_random_string()
    my_acc_signed_out_page.type_login_username(login_value)
    my_acc_signed_out_page.type_login_password(password)
    my_acc_signed_out_page.click_on_login_button()
    return login_value

@then(parsers.parse('the system should display the correct invalid login error message for "{credential_type}"'))
def verify_invalid_message(my_acc_signed_out_page:MyAccountSignedOutPage,credential_type,login_value):
    expected =""
    actual=""
    if credential_type == "email":
        expected = "Unknown email address. Check again or try your username."
        actual = my_acc_signed_out_page.get_invalid_login_error_email()
    elif credential_type == "username":
        expected = f"Error: The username {login_value} is not registered on this site. If you are unsure of your username, try your email address instead."
        actual = my_acc_signed_out_page.get_invalid_login_error_username()

    assert expected == actual,(f"Test Negative Verify Invalid Login Message has failed. "
                               f"Expected Login Error message does not match the actual error message. "
                               f"Expected: {expected}, "
                               f"Actual: {actual}")
@scenario('tests/ui_tests/features/negative_invalid_login_message_.feature','A user cannot login with invalid credentials')
def test_negative_verify_invalid_login_message():
    pass