Feature: Discount by Coupon
  Scenario: I should be able to apply coupon after creating in API
    Given I have a product
    And  I have a fixed-cart discount coupon

    When I navigate to product page
    And I add the product to cart
    And I apply the coupon

    Then The total price should be reduced by the coupon amount

