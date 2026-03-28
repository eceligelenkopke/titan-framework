Feature: Creating Order via API
  Scenario: I should create order via api and verify it exists in database

    Given I have a product

    When I make an order via API

    Then Order details should match details in database