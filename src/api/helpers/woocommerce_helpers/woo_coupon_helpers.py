from src.api.helpers.woocommerce_helpers.woo_payload_helpers import WooPayloadHelpers
from src.api.clients.woo_api_client import WooAPIClient
class WooCouponHelpers:
    def __init__(self):
        self.woo_api_client = WooAPIClient()
        self.woo_payload_helpers = WooPayloadHelpers()
        self.endpoint = "coupons/"

    def create_a_coupon(self, coupon_code=None, discount_type=None, discount_amount=None,**kwargs):
        coupon_payload = self.woo_payload_helpers.create_a_coupon_payload(
            coupon_code=coupon_code,
            discount_type=discount_type,
            discount_amount=discount_amount,
            **kwargs
        )
        return self.woo_api_client.post(wc_endpoint=self.endpoint, data=coupon_payload)

    def get_all_coupons(self):
        return self.woo_api_client.get(self.endpoint)

    def get_a_coupon_by_id(self,coupon_id):
        endpoint = self.endpoint+str(coupon_id)
        return self.woo_api_client.get(wc_endpoint=endpoint)

    def update_a_coupon(self,coupon_id,**kwargs):
        endpoint = self.endpoint+str(coupon_id)
        rs_api = self.woo_api_client.put(endpoint,kwargs)
        return rs_api

    def delete_a_coupon_from_api(self,coupon_id,expected_status_code=None):
        try:
            rs_api = self.woo_api_client.delete(self.endpoint+str(coupon_id),
                                                expected_status_code=expected_status_code)
            return rs_api
        except AssertionError:
            if not self.woo_api_client.status_code == 404:
                raise
            return self.woo_api_client.rs_json