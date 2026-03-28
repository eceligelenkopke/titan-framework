Feature: Cart Page Coupon Application
  Scenario: I should be unable to apply an invalid coupon

    Given I have a product

    When I navigate to product page
    And I add the product to cart
    And I try to apply an invalid coupon

    Then I should verify invalid coupon message
