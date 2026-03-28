Feature: API holds email value correctly
Scenario: Create a new user via API and verify email existence
    When I create a customer
    Then the returned user data should contain a valid email