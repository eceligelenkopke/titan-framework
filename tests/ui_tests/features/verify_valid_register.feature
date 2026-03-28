Feature: User Registration

  Scenario: A new user can successfully register an account

    When I register with valid email and password

    Then the system should log me in and display the account details dashboard