Feature: Product Reviews

  Scenario: A user can submit a review and see it awaiting approval
    Given I have a product
    When I navigate to product page
    And I submit a new review for the product
    Then the review should be displayed with an awaiting approval status