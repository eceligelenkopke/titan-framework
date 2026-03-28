from pytest_bdd import when,then,scenario
from src.ui.pages.home_page import HomePage
from src.api.helpers.general_helpers import create_random_string

@when('I search for a randomly generated non-existent product')
def search_for_non_existing_product(home_page:HomePage):
    invalid_product = create_random_string()
    home_page.click_on_search_products()
    home_page.search_a_product(invalid_product)
    home_page.click_on_search_button()


@then('the system should display a no products found error message')
def verify_no_products_found_message(home_page:HomePage):
    expected = "No products were found matching your selection."
    actual = home_page.get_no_product_found_message()

    assert expected == actual,(f"Test Negative Verify Search invalid Product Message has failed. "
                               f"Expected not found message does not match the Actual not found message. "
                               f"Expected: {expected}, "
                               f"Actual: {actual}")



@scenario('tests/ui_tests/features/negative_verify_search_invalid_product_message.feature','A user searches for a non-existent product')
def test_negative_verify_invalid_product_message():
    pass