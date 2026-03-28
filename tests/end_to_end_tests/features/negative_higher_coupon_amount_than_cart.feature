Feature: Cart Section Discount Calculation
  Scenario: Total Price can not be negative

    Given I have a product whose price is 30$
    And I have a whose value exceeds the product price discount coupon

    When I navigate to product page
    And I add the product to cart
    And I apply the coupon
    And I make the order

    Then Total Price with Coupon cannot be negative



