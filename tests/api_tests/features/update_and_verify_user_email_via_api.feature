Feature: Update User Payload Using API
  Scenario: I should be able to update user email via API

    Given I have a customer

    When I update the customer email

    Then Updated email should be different than the Initial email
    And And the customer details should reflect the new email