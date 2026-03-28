Feature: Login Management

  Scenario Outline: A user cannot login with invalid credentials
    Given I navigate to the my account signed out page
    When I attempt to login with an unregistered "<credential_type>"
    Then the system should display the correct invalid login error message for "<credential_type>"

    Examples:
      | credential_type |
      | username        |
      | email           |