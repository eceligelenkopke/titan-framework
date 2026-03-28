from src.api.helpers.woocommerce_helpers.woo_payload_helpers import WooPayloadHelpers
from src.api.clients.woo_api_client import WooAPIClient
from src.database.dao.woocommerce_dao.woo_products_dao import WooProductsDao
from src.api.helpers.general_helpers import create_random_string
import random
class WooProductHelpers:
    def __init__(self):
        self.woo_payload_helpers = WooPayloadHelpers()
        self.woo_api_client = WooAPIClient()
        self.endpoint = "products/"
        self.products_dao = WooProductsDao()

    def create_a_product_in_api(self,product_name=None,product_type=None,regular_price=None,stock_quantity=None, **kwargs):
        random_product = self.woo_payload_helpers.create_random_product_payload(
            product_name=product_name,
            product_type=product_type,
            regular_price=regular_price,
            stock_quantity=stock_quantity,
            **kwargs
        )

        rs_api = self.woo_api_client.post(data=random_product, wc_endpoint=self.endpoint, expected_status_code=201)
        assert rs_api,"API Response is EMPTY!"
        return rs_api

    def get_regular_price_value_by_id_from_api(self,product_id):
        product_id = str(product_id)
        price_value = self.woo_api_client.get(self.endpoint + product_id)
        return float(price_value['regular_price'])

    def get_a_product_by_id_via_api(self,product_id,expected_status_code=None):
        if not expected_status_code:
            expected_status_code = 200
        product_id = str(product_id)
        rs_api = self.woo_api_client.get(self.endpoint + product_id, expected_status_code=expected_status_code)
        return rs_api

    def delete_a_product_by_id_via_api(self,product_id,expected_status_code=None):
        try:
            rs_api = self.woo_api_client.delete(self.endpoint + str(product_id),
                                                expected_status_code=expected_status_code)
            return rs_api
        except AssertionError:
            if not self.woo_api_client.status_code == 404:
                raise
            return self.woo_api_client.rs_json

    def update_a_product_via_api(self,product_id,**kwargs):
        product_id = str(product_id)
        rs_api = self.woo_api_client.put(self.endpoint + product_id, kwargs, expected_status_code=200)
        return rs_api

    def make_a_product_review(self,**kwargs):
        endpoint = self.endpoint + "reviews"
        rs_api = self.woo_api_client.post(endpoint,kwargs)
        return rs_api