Feature: Update Price and Name via API
  Scenario: I should be able to update and price values via API

    Given I have a product

    When I update the product price and name

    Then Price and Name values should be updated



