import pytest
import allure
from src.selenium.core.webdriver_provider import WebDriverProvider
from src.api.helpers.woocommerce_helpers.woo_product_helpers import WooProductHelpers
from src.api.helpers.woocommerce_helpers.woo_coupon_helpers import WooCouponHelpers
from src.api.helpers.woocommerce_helpers.woo_customer_helpers import WooCustomerHelpers
from src.api.helpers.woocommerce_helpers.woo_order_helpers import WooOrderHelpers
from src.database.dao.woocommerce_dao.woo_customers_dao import WooCustomersDao
from src.database.dao.woocommerce_dao.woo_orders_dao import WooOrdersDao
from src.database.dao.woocommerce_dao.woo_products_dao import WooProductsDao
from src.database.dao.woocommerce_dao.woo_coupons_dao import WooCouponsDao
@pytest.fixture()
def woo_coupon_helpers():
    return WooCouponHelpers()
@pytest.fixture()
def woo_product_helpers():
    return WooProductHelpers()
@pytest.fixture()
def woo_order_helpers():
    return WooOrderHelpers()
@pytest.fixture()
def woo_customer_helpers():
    return WooCustomerHelpers()
@pytest.fixture()
def woo_products_dao():
    return WooProductsDao()
@pytest.fixture()
def woo_coupons_dao():
    return WooCouponsDao()
@pytest.fixture()
def woo_orders_dao():
    return WooOrdersDao()
@pytest.fixture()
def woo_customers_dao():
    return WooCustomersDao()

pytest_plugins = [
    "tests.common_steps.api_common_steps",
    "tests.common_steps.ui_common_steps"
]

def pytest_runtest_teardown(item, nextitem):
    WebDriverProvider.quit_driver()

def pytest_collection_modifyitems(items):
    """
    Dynamically assigns Allure Epics based on the test directory structure.
    """
    for item in items:
        if "ui_tests" in item.nodeid:
            item.add_marker(allure.epic("UI Tests"))
        elif "api_tests" in item.nodeid:
            item.add_marker(allure.epic("API Tests"))
        elif "end_to_end_tests" in item.nodeid:
            item.add_marker(allure.epic("END_TO_END Tests"))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when in ["setup", "call"] and report.failed:
        driver = WebDriverProvider._driver
        if driver is not None:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"{item.name}.png",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                print(
                    f"\n📸 [Warning] Failed to take screenshot for {item.name}. The browser window might have already been closed or crashed.")

@pytest.fixture()
def resource_registry(woo_product_helpers:WooProductHelpers, woo_customer_helpers:WooCustomerHelpers, woo_order_helpers:WooOrderHelpers, woo_coupon_helpers:WooCouponHelpers):
    resources = {
        "product":[],
        "coupon":[],
        "order":[],
        "customer":[]
    }
    yield resources
    for resource_id in resources['product']:
        try:
            woo_product_helpers.delete_a_product_by_id_via_api(resource_id)
        except Exception:
            pass
    for resource_id in resources['order']:
        try:
            woo_order_helpers.delete_an_order_via_api(resource_id)
        except Exception:
            pass
    for resource_id in resources['customer']:
        try:
            woo_customer_helpers.delete_customer_from_api(resource_id)
        except Exception:
            pass
    for resource_id in resources['coupon']:
        try:
            woo_coupon_helpers.delete_a_coupon_from_api(resource_id)
        except Exception:
            pass