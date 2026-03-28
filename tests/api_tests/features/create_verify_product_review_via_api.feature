Feature: WooCommerce Create Review
  Scenario: I should be able to create a product review via API
    Given I have a product

    When I make a product review

    Then Review should be created
    And Review details should match

