Feature: Cart Calculations

  Scenario: Cart total updates dynamically when product quantity is increased
    Given I have a product
    And I navigate to product page

    When I get the product details from the product page
    And I add the product to cart
    And I increase the product quantity

    Then the cart total price should update to reflect the new quantity