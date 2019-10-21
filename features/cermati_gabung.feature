Feature: Join into cermati.com

Scenario: Sign up into cermati.com
  Given I am on cermati gabung page
    And I input my email
    And I input my password
    And I input my first name
    And I input my last name
    And I input my mobile phone
    And I input my residence city
  When  I click submit join button
  Then  The validation success appears
