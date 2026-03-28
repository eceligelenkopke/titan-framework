from pytest_bdd import when,then,given,scenario
from src.api.helpers.woocommerce_helpers.woo_product_helpers import WooProductHelpers
from src.database.dao.woocommerce_dao.woo_products_dao import WooProductsDao
from src.ui.pages.cart_page import CartPage


@when('I update the cart quantity',target_fixture="test_data")
def update_quantity(cart_page:CartPage,product):
    initial_stock = product['stock_quantity']
    cart_page.delete_existing_quantity_value()
    cart_page.update_quantity_value(quantity_value=4)
    cart_page.wait_until_cart_updated_message_visible()
    updated_quantity = cart_page.get_existing_quantity_value()
    test_data = {
        "initial_stock":initial_stock,
        "updated_quantity":updated_quantity
    }
    return test_data


@then('Stock values should be updated correctly')
def verify_stock_initial_value(woo_products_dao:WooProductsDao,test_data,product,woo_product_helpers:WooProductHelpers):
    updated_product = woo_product_helpers.get_a_product_by_id_via_api(product['id'])
    quantity = test_data['updated_quantity']
    initial_stock = test_data['initial_stock']
    updated_stock = int(updated_product['stock_quantity'])
    stock_in_db = woo_products_dao.get_the_stock_quantity_via_product_id(product['id'])


    assert updated_stock + quantity == initial_stock,(f"Test Create a Product via API buy via UI verify Stock in DB has failed. "
                                                      f"Quantity added to Updated Stock Value does not match the Initial Stock Value. "
                                                      f"Updated Stock Value: {updated_stock}, Quantity: {quantity}, Total: {updated_stock+quantity}, "
                                                      f"Initial Stock Value: {initial_stock},"
                                                      f"Difference: {initial_stock - (updated_stock+quantity)}")
    assert updated_stock == stock_in_db,(f"Test Create a Product via API buy via UI verify Stock in DB has failed. "
                                         f"Updated Stock in API does not match the Current Stock in DB. "
                                         f"Stock in API: {updated_stock}, "
                                         f"Stock in DB: {stock_in_db}")




@scenario('tests/end_to_end_tests/features/create_product_via_api_buy_ui_verify_stock_db.feature','The stock amount should reduce to expected amount')
def test_create_product_via_api_buy_ui_verify_stock_via_db():
    pass