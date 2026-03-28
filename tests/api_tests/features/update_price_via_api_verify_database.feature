Feature: WooCommerce Products API Management
  Scenario: Update a random product's regular price and verify data consistency across API and DB
    Given I have a product
    When I update the price values

    Then the initial price values should match
    And the price should be updated correctly in database
