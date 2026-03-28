Feature: Order Status Management
  Scenario: I should be able to update order status via API
    Given I have a product
    And I make an order via API

    When I update the order status

    Then The Order status should be updated
    And The Order should have the expected product

