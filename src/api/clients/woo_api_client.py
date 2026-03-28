from src.api.helpers.config_helpers import ConfigHelper
from woocommerce import API
class WooAPIClient:
    def __init__(self):
        config_helper = ConfigHelper()
        api_credentials = config_helper.get_api_credentials()
        self.base_url = config_helper.get_base_url()
        self.wcapi = API(
            url=self.base_url,
            consumer_key=api_credentials['WC_KEY'],
            consumer_secret=api_credentials['WC_SECRET'],
            version="wc/v3",
            timeout=10
        )
    def assert_status_code(self):
        assert self.expected_status_code == self.status_code,(f"Expected: {self.expected_status_code}, Actual Code: {self.status_code},"
                                                              f"Url: {self.endpoint}, Response JSON = {self.rs_json}")
    def get(self,wc_endpoint,params=None,expected_status_code=200):
        rs_api = self.wcapi.get(endpoint=wc_endpoint,params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()
        return self.rs_json

    def put(self, wc_endpoint, data=None, expected_status_code=200):
        rs_api = self.wcapi.put(endpoint=wc_endpoint,data=data)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()
        return self.rs_json

    def post(self, wc_endpoint, data=None, expected_status_code=201):
        rs_api = self.wcapi.post(endpoint=wc_endpoint,data=data)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()
        return self.rs_json

    def delete(self, wc_endpoint, params=None, expected_status_code=None):
        if not params:
            params = {'force': True }
        if not expected_status_code:
            expected_status_code = 200
        rs_api = self.wcapi.delete(endpoint=wc_endpoint,params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()
        return self.rs_json

