from pytest_bdd import when,then,scenario
from src.api.helpers.woocommerce_helpers.woo_product_helpers import WooProductHelpers
from src.api.helpers.general_helpers import generate_random_email,create_random_string
import random

@when('I make a product review',target_fixture='review_elements')
def make_a_product_review(woo_product_helpers:WooProductHelpers,product):
    product_id = product['id']
    review_payload = {
        "product_id":product_id,
        "review":create_random_string(),
        "reviewer":create_random_string(string_length=3)+" "+create_random_string(string_length=5),
        "reviewer_email":generate_random_email(),
        "rating":random.randint(1,5)
    }
    rs_api = woo_product_helpers.make_a_product_review(**review_payload)
    review_elements = {
        "api_response":rs_api,
        "review_payload":review_payload
    }
    return review_elements

@then('Review should be created')
def verify_review_created(review_elements):
    rs_api = review_elements['api_response']
    assert "id" in rs_api, (f"Test Create and Verify a Product Review via API has failed. "
                    f"Unable to get a valid response from API. "
                    f"Actual: {rs_api}")

@then('Review details should match')
def verify_reviews_details_match(review_elements):
    rs_api = review_elements['api_response']
    payload = review_elements['review_payload']

    payload_review = payload['review']
    api_review = rs_api['review']
    assert payload_review == api_review, (f"Test Create and Verify a Product Review via API has failed. "
                                          f"Review in API does not match the Review in payload. "
                                          f"Review in API: {api_review}, "

                                          f"Review in Payload: {payload_review}")
    payload_id = payload['product_id']
    api_id = rs_api['product_id']
    assert  payload_id == api_id, (f"Test Create and Verify a Product Review via API has failed. "
                                   f"Product ID in API does not match the Product ID in Payload. "
                                   f"ID in API: {api_id}, "
                                   f"ID in Payload: {payload_id}")

    payload_email = payload['reviewer_email']
    api_email = rs_api['reviewer_email']
    assert payload_email == api_email, (f"Test Create and Verify a Product Review via API has failed. "
                                  f"Reviewer Email in API does not match the Reviewer Email in Payload. "
                                  f"ID in API: {api_email}, "
                                  f"ID in Payload: {payload_email}")




@scenario('tests/api_tests/features/create_verify_product_review_via_api.feature','I should be able to create a product review via API')
def test_create_a_product_review_via_api_verify_created():
    pass