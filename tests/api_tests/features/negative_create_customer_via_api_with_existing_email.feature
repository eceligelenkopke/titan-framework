Feature: Unable to Register with Existing Email

  Scenario: I should not be able to register with an existing email
    Given I create a customer
    And I get the existing user email

    When I try to register with existing user email

    Then The user should not be registered
