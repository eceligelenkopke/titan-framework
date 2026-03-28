Feature: Product Search

  Scenario: A user searches for a non-existent product
    Given I navigate to the home page
    When I search for a randomly generated non-existent product
    Then the system should display a no products found error message