Feature: Edit Book
  Scenario: Edit book informations
    Given the user is in the profile page and scroll into the registered books
    When clicks in Edit and edit some book information
    Then system updates the book information
