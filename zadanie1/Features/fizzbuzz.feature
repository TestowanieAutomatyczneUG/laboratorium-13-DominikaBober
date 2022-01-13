Feature: FizzBuzz

    Scenario: FizzBuzz gets 3
    Given Play FizzBuzz
    When Give 3
    Then Get Fizz

    Scenario: FizzBuzz gets 5
    Given Play FizzBuzz
    When Give 5
    Then Get Buzz

    Scenario: FizzBuzz gets 15
    Given Play FizzBuzz
    When Give 15
    Then Get FizzBuzz

    Scenario: FizzBuzz gets 34
    Given Play FizzBuzz
    When Give 34
    Then Get 34

    Scenario: FizzBuzz gets 555
    Given Play FizzBuzz
    When Give 555
    Then Get FizzBuzz

    Scenario: FizzBuzz gets 0
    Given Play FizzBuzz
    When Give 0
    Then Get FizzBuzz
