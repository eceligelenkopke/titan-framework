from pytest_bdd import then,scenario



@then('the system should display a success message containing the product name')
def verify_success_message(product,added_to_cart_message):
    expected = f'“{product['name']}” has been added to your cart.'
    actual = added_to_cart_message
    assert expected in actual, (f"Test Verify Product Added to Cart has failed. "
                                f"Expected Added to Cart Message does not match the Added to Cart Message in Product Page. "
                                f"Expected: {expected}, "
                                f"Actual: {actual}")

@then('the cart page should display the correct product details')
def verify_cart_page_product_details(product,ui_product_values):
    ui_name = ui_product_values['name']
    api_name = product['name'].lower()
    assert ui_name == api_name,(f"Test Verify Product Added to Cart has failed. "
                                f"Product name in UI does not match the Product name in API. "
                                f"UI Name: {ui_name}, "
                                f"API Name: {api_name}")
    ui_price = ui_product_values['price']
    api_price = float(product['regular_price'])

    assert ui_price == api_price,(f"Test Verify Product Added to Cart has failed. "
                                f"Product Price in UI does not match the Product Price in API. "
                                f"UI Price: {ui_price}, "
                                f"API Price: {api_price}")





@scenario('tests/ui_tests/features/verify_product_added_to_cart.feature','A user can successfully add a product to the cart')
def test_verify_product_added_to_cart():
    pass