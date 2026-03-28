Feature: Database Order Verification

  Scenario: Create product via API, buy it via UI, and verify order via DB
    Given I have a product
    And I register with valid email and password

    When I navigate to product page
    And I add the product to cart
    And I make the order

    Then the order details should be recorded correctly in the database
