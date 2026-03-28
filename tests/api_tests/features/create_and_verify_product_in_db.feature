Feature: Product Management
  Scenario: Create a random product via API and verify in Database
    When I create a product
    Then the product details in the database should match the created product



