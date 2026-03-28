Feature: Stock Management
  Scenario: The stock amount should reduce to expected amount
    Given I have a product

    When I navigate to product page
    And I add the product to cart
    And I update the cart quantity
    And I make the order

    Then Stock values should be updated correctly

