Feature: Coupon Usage Limits

  Scenario: A single-use coupon cannot be applied a second time after being consumed
    Given I have a product
    And I have a one usage limit discount coupon

    When I navigate to product page
    And I add the product to cart
    And I apply the coupon
    And I make the order

    And I navigate to product page
    And I add the product to cart
    And I attempt to apply the coupon again
    Then the system must reject the coupon with a usage limit error message