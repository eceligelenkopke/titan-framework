Feature: Verify API Created Product Exists in UI
  Scenario: I should see the product created
    Given I have a product

    When I navigate to product page
    And I get the product details from the product page

    Then Product details should match the created product details
