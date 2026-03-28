Feature: Verify Coupon created via API Applied in UI verified in DB
  Scenario: I create a coupon via API, apply via UI and verify via DB
  Given I have a coupon
  And I have a product

    When I register with valid email and password
    And I navigate to product page
    And I add the product to cart
    And I apply the coupon
    And I make the order
    Then Coupon should be applied successfully