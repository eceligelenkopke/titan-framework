from pytest_bdd import then,scenario
from src.ui.pages.product_page import ProductPage

@then('Product details should match the created product details')
def verify_product_details(ui_product_values,product):
    title_in_ui = ui_product_values['name']
    title_in_api = product['name'].lower()
    price_in_ui = ui_product_values['price']
    price_in_api = float(product['regular_price'])

    assert title_in_ui == title_in_api,(f"Test Create Product via API and Verify Exists in UI has failed. "
                                        f"Title in UI does not match the title in API. "
                                        f"Title in UI: {title_in_ui}, "
                                        f"Title in API: {title_in_api}")

    assert price_in_ui == price_in_api,(f"Test Create Product via API and Verify Exists in UI has failed. "
                                        f"Price in UI does not match the Price in API. "
                                        f"Price in UI: {price_in_ui}, "
                                        f"Price in API: {price_in_api}")

@scenario('tests/end_to_end_tests/features/create_product_api_verify_exists_in_ui.feature','I should see the product created')
def test_create_product_api_verify_exists_in_ui():
    pass