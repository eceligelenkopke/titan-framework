Feature: Delete and Verify Product Deleted
  Scenario: I should delete a product and verify it is deleted

    Given I have a product

    When I delete the product

    Then The Product should be deleted