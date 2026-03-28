Feature: Order Creation and Synchronization

  Scenario: A completed UI order should be correctly recorded in the system backend
    Given I have a product

    When I navigate to product page
    And I add the product to cart
    And I make the order

    Then the order should be successfully created in the system with the matching checkout price