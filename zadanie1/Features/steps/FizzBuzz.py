import sys
sys.path.append('./zadanie1')
from behave import *
from src.FizzBuzz import FizzBuzz

use_step_matcher("parse")

@given('Play FizzBuzz')
def step_impl(context):
    context.FizzBuzz = FizzBuzz()

@when(u'Give {number}')
def step_impl(context, number):
    context.result = context.FizzBuzz.play(int(number))

@then('Get FizzBuzz')
def step_impl(context):
    assert context.result == "FizzBuzz"

@then('Get Fizz')
def step_impl(context):
    assert context.result == "Fizz"

@then('Get Buzz')
def step_impl(context):
    assert context.result == "Buzz"

@then('Get {result}')
def step_impl(context, result):
    assert context.result == result
