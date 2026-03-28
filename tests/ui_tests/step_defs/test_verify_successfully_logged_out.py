from pytest_bdd import when,then,scenario
from src.ui.pages.my_account_signed_out import MyAccountSignedOutPage
from src.ui.pages.my_account_signed_in import MyAccountSignedInPage

@when('I click on the logout button')
def click_on_logout_button(my_acc_signed_in_page:MyAccountSignedInPage):
    my_acc_signed_in_page.click_on_log_out_button()

@then('the system should successfully log me out and display the login form')
def verify_logged_out(my_acc_signed_out_page:MyAccountSignedOutPage):
    is_visible = my_acc_signed_out_page.scroll_until_login_button_seen()
    assert is_visible,(f"Test Verify Successfully Logged Out has failed. "
                               f"Unable to see the LOGIN buton after Logged OUT.")
@scenario('tests/ui_tests/features/verify_successfully_logged_out.feature','A user can successfully log out of their account')
def test_verify_logged_out():
    pass