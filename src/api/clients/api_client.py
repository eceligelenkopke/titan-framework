import json
import os
import requests
from requests_oauthlib import OAuth1
from src.api.helpers.config_helpers import ConfigHelper

class APIClient:
    def __init__(self):
        pass
        self.env = os.environ.get("ENV","test")
        config_helpers = ConfigHelper()
        self.base_url = config_helpers.get_base_url()
        api_credentials = config_helpers.get_api_credentials()
        self.auth = OAuth1(api_credentials["WC_KEY"],api_credentials["WC_SECRET"])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code,(f"Bad Status Code.\n"
                                                             f"Expected: {self.expected_status_code}, Actual Code:{self.status_code}"
                                                             f"Url: {self.url}, Response Json: {self.rs_json}")

    def get(self, endpoint, payload=None,headers=None,expected_status_code=200):
        if not headers:
            headers = {"Content-Type":"application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.get(self.url,data=json.dumps(payload),headers=headers,auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        return self.rs_json

    def post(self, endpoint,payload=None,headers=None,expected_status_code=201):
        if not headers:
            headers = {"Content-Type":"application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.post(self.url,data=json.dumps(payload),headers=headers,auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        return self.rs_json


    def put(self, endpoint,payload=None,headers=None,expected_status_code=200):
        if not headers:
            headers = {"Content-Type":"application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.put(url=self.url,data=json.dumps(payload),headers=headers,auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        return self.rs_json

    def delete(self,endpoint,payload=None,headers=None,expected_status_code=200):
        if not headers:
            headers = {"Content-Type":"application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.delete(url=self.url,data=json.dumps(payload),headers=headers,auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        return self.rs_json