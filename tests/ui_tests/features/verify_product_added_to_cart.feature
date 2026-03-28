Feature: Cart Management

  Scenario: A user can successfully add a product to the cart

    Given I have a product

    When I navigate to product page
    And I get the product details from the product page
    And I add the product to cart

    Then the system should display a success message containing the product name
    And the cart page should display the correct product details
