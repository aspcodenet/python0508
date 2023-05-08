from behave import *
from app import *

@given("the user is already registered")
def step_impl(context):
    context.email = "stefan.holmberg@systementor.se"    
    context.sut = UserRegistrationService()
    context.sut.Users.append(User("stefan.holmberg@systementor.se","Stefan"))

@when("the user registers")
def step_impl(context):
    context.result = context.sut.Register(context.email, "Stefan")

@then("there should be an error")
def step_impl(context):
    assert(context.result == False)




@given("the user is not already registered")
def step_impl(context):
    context.email = "stefan.holmberg@systementor.se"    
    context.sut = UserRegistrationService()
    context.sut.Users = []

@then("there should not be an error")
def step_impl(context):
    assert(context.result == True)





@then("the user should exist")
def step_impl(context):
    assert(context.sut.Find(context.email) != None)


