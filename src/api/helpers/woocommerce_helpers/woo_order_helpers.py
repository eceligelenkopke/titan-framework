from src.database.dao.woocommerce_dao.woo_orders_dao import WooOrdersDao
from src.api.clients.woo_api_client import WooAPIClient
from src.api.helpers.woocommerce_helpers.woo_product_helpers import WooProductHelpers
from src.api.helpers.woocommerce_helpers.woo_payload_helpers import WooPayloadHelpers

class WooOrderHelpers:
    def __init__(self):
        self.woo_api_client = WooAPIClient()
        self.orders_dao = WooOrdersDao()
        self.endpoint = 'orders/'
        self.woo_product_helpers = WooProductHelpers()
        self.woo_payload_helpers = WooPayloadHelpers()

    def get_an_order_by_order_id(self,order_id):
        endpoint = self.endpoint + str(order_id)
        return self.woo_api_client.get(endpoint)

    def create_an_order_via_api(self,product_id,**kwargs):
        order_payload = self.woo_payload_helpers.create_random_order_payload(product_id=product_id,**kwargs)
        return self.woo_api_client.post(self.endpoint,data=order_payload)

    def update_an_order_via_api(self,order_id,**kwargs):
        endpoint = self.endpoint+str(order_id)
        return self.woo_api_client.put(endpoint,data=kwargs)

    def delete_an_order_via_api(self,order_id,expected_status_code=None):
        try:
            rs_api = self.woo_api_client.delete(self.endpoint + str(order_id),
                                                expected_status_code=expected_status_code)
            return rs_api
        except AssertionError:
            if not self.woo_api_client.status_code == 404:
                raise
            return self.woo_api_client.rs_json



