from behave import *
from cucumber_basket.cucumber_basket import CucumberBasket

@given(u'the basket has “{n}” cucumbers')
def step_impl(context,n):
    context.c = CucumberBasket(n)


@when(u'"4" cucumbers are added to the basket')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When "4" cucumbers are added to the basket')


@then(u'the basket contains "9" cucumbers')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the basket contains "9" cucumbers')
