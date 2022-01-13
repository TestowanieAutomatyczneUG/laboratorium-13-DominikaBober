from behave import *

@when('Set planet 1st planet')
def step_impl(context):
    context.Planets.set_planet("merkury")

@when('Set planet 2nd planet')
def step_impl(context):
    context.Planets.set_planet("wenus")

@when('Set planet 3th planet')
def step_impl(context):
    context.Planets.set_planet("ziemia")

@when('Set planet 4th planet')
def step_impl(context):
    context.Planets.set_planet("mars")

@when('Set planet 5th planet')
def step_impl(context):
    context.Planets.set_planet("jowisz")

@when('Set planet 6th planet')
def step_impl(context):
    context.Planets.set_planet("saturn")

@when('Set planet 7th planet')
def step_impl(context):
    context.Planets.set_planet("uran")

@when('Set planet 8th planet')
def step_impl(context):
    context.Planets.set_planet("neptun")

@then(u'Set time {time}')
def step_impl(context, time):
    context.result = context.Planets.give_time(float(time))

@step(u'Get {time}')
def step_impl(context, time):
    assert context.result == float(time)
