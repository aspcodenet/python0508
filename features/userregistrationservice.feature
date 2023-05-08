Feature: User registration

    Scenario: Register an already existing user
        Given the user is already registered
        When the user registers
        Then there should be an error

    Scenario: Register an not existing user
        Given the user is not already registered
        When the user registers
        Then there should not be an error
        And the user should exist

