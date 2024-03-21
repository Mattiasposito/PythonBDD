from behave import given, when, then


@given("Launch the App and Click on Login Button")
def methodOne(context):
    print("L1 - Launching the App")


@when("Enter {emailid} UserID")
def methodTwo(context,emailid):
    print("L2 - Enter the UserID in Login Screen {} ".format(emailid))


@when("Enter {pasw} password")
def methodThree(context,pasw):
    print("L3 - Enter the Password {} in Login Screen".format(pasw))


@then("Verify {screen} Screen")
def methodFour(context,screen):
    print("L4 - {} screen".format(screen))
