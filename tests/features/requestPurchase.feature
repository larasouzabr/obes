Feature: Request Purchase
  Scenario: Request book purchase
    Given institutional or common user is in the homepage
    When clicks in some available book and clicks in Add to Cart
    Then system shows the message that the product has been added to cart