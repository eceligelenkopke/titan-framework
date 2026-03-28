from src.api.clients.woo_api_client import WooAPIClient
from src.api.helpers.woocommerce_helpers.woo_payload_helpers import WooPayloadHelpers
class WooCustomerHelpers:
    def __init__(self):
        self.woo_api_client = WooAPIClient()
        self.endpoint = "customers/"
        self.woo_payload_helpers = WooPayloadHelpers()

    def create_customer_in_api(self,expected_status_code=None,**kwargs):
        if not expected_status_code:
            expected_status_code = 201
        payload = self.woo_payload_helpers.create_a_customer_payload(**kwargs)
        return self.woo_api_client.post(self.endpoint,payload,expected_status_code=expected_status_code)

    def get_customer_by_id_from_api(self,customer_id):
        return self.woo_api_client.get(self.endpoint+str(customer_id))

    def update_customer_from_api(self,customer_id,**kwargs):
        customer_id = str(customer_id)
        return self.woo_api_client.put(self.endpoint+customer_id,data=kwargs)

    def delete_customer_from_api(self,customer_id,expected_status_code=None):
        try:
            rs_api = self.woo_api_client.delete(self.endpoint + str(customer_id),
                                                expected_status_code=expected_status_code)
            return rs_api
        except AssertionError:
            if not self.woo_api_client.status_code == 404:
                raise
            return self.woo_api_client.rs_json

    def get_all_customers(self):
        return self.woo_api_client.get(self.endpoint)



