Feature: Close account

  Scenario: I want to close an account
    Given there an "active" account with customer id "12345"
    When I get the account details for account "1"
    When I close the account with ID "1"
    Then my account should be "closed" and have customer ID "12345"
