#this is a feature file


Feature: Verify the home Screen Data

  Scenario: User Login credentials

    Given Launch the App and click on login Button
    When Enter UserID
    When Enter password
    When Click on Login Button
    And Home page opens
    Then Verify Home Screen
    Then Take screenshot

  Scenario: Enter the data in Contact Form

    Given Launch the App and Click on ContactForm
    When Enter Name
    When Enter Email
    When Enter Mobile Number
    And we need to click on submit button
    Then Click on submit
    Then Take Screenshot of contact Form
