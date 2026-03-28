Feature: End to End Shopping Flow

  Scenario: A newly registered user can successfully place an order with a coupon
    Given I have a product
    And I have a fixed-cart discount coupon

    When I register with valid email and password
    And I navigate to product page
    And I add the product to cart
    And I apply the coupon
    And I make the order
    Then the order should be successfully placed and received