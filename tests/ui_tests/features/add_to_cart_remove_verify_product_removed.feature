Feature: Cart Page Item Management

  Scenario: A user can successfully remove an item from their cart
    Given I have a product

    When I navigate to product page
    And I add the product to cart
    And I remove the product from the cart

    Then the cart should display a product removed confirmation message
    And the cart should be completely empty