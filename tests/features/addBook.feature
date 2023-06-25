Feature: Add Book
  Scenario: Add Book for donation
    Given user in the Add Book page
    When fills out all the required information and clicks in Next
    Then systems add book to donation page