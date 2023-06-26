Feature: Request Donation
  Scenario: Book donation request
    Given institutional user is in the homepage
    When clicks in some available book and clicks in Request Donation
    Then system adds book to orders page