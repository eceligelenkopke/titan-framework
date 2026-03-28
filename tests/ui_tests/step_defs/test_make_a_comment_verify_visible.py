from pytest_bdd import when,then,scenario

from src.ui.pages.product_page import ProductPage
from src.api.helpers.general_helpers import create_random_string, generate_random_email


@when('I submit a new review for the product',target_fixture='review')
def submit_a_review(product_page:ProductPage):
    review = create_random_string()
    name = create_random_string()
    email = generate_random_email()
    product_page.click_on_review_button()
    product_page.give_stars()
    product_page.make_a_comment(review)
    product_page.type_comment_name(name)
    product_page.type_comment_email(email)
    product_page.click_on_submit_button()
    return review

@then('the review should be displayed with an awaiting approval status')
def verify_review_message(review,product_page:ProductPage):
    expected_approval = "Your review is awaiting approval"
    actual_approval = product_page.review_waiting_approval_message()
    actual_review = product_page.get_review_message_text()
    expected_review = review
    assert expected_approval == actual_approval,(f"Test Make a Comment Verify Visible has failed. "
                                                 f"Expected Approval Message does not match the Approval Message in UI. "
                                                 f"Expected: {expected_approval}, "
                                                 f"Actual: {actual_approval}")

    assert expected_review == actual_review,(f"Test Make a Comment Verify Visible has failed. "
                                             f"Expected Review does not match the Review Message seen in UI. "
                                             f"Expected: {expected_review}, "
                                             f"Actual: {actual_review}")

@scenario('tests/ui_tests/features/make_a_comment_verify_visible.feature','A user can submit a review and see it awaiting approval')
def test_make_a_comment_verify_visible():
    pass