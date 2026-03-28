Feature: Out of Stock
  Scenario: I should be unable to buy an out-of-stock product
    Given I have a product with one stock

    When I navigate to product page
    And I add the product to cart
    And I proceed to the checkout field
    And the product becomes out of stock in the background
    And I attempt to place the order

    Then the order should be rejected with an out-of-stock error message