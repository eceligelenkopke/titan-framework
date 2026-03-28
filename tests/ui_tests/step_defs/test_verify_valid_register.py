from pytest_bdd import then,scenario
from src.ui.pages.my_account_signed_in import MyAccountSignedInPage

@then('the system should log me in and display the account details dashboard')
def verify_register_valid(my_acc_signed_in_page:MyAccountSignedInPage):
    is_visible = my_acc_signed_in_page.verify_signed_in_by_acc_details_button()
    assert is_visible,(f"Test Verify Valid Register has failed. "
                               f"Unable to get the Account Details Button in Dashboard and Unable to Register.")
@scenario('tests/ui_tests/features/verify_valid_register.feature','A new user can successfully register an account')
def test_verify_valid_register():
    pass
