Feature: User Registration and Data Security
  Scenario: A newly registered user's credentials should be securely stored in the database
    When I register with valid email and password

    Then the user account should be successfully created in the database
    And the user password must be stored securely as encrypted data