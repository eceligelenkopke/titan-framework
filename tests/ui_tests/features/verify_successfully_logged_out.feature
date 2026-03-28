Feature: Log Out Management

  Scenario: A user can successfully log out of their account
    Given I register with valid email and password

    When I click on the logout button
    Then the system should successfully log me out and display the login form