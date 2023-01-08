# QUESTION 2.2:
# Your boss really likes calculating VAT on their purchases. It is their favourite hobby.
# They've written this code to calculate VAT and need your help to fix it.

# def calculate_vat(amount):
#   amount * 1.2
#   total = calculate_vat(100)
# print(total)

# When your boss runs the program they get the following output:
# None
# Your boss expects the program to output the value 120. What is wrong? How do you fix it?

# ANSWER:
# def statement creates a function with the function name "calculate_vat" and the parameter "amount".
def calculate_vat(amount):
    # The indented statements are the function body, and are executed each time the function is called.
    # In the original function body, the "total" variable was defined incorrectly and included the function call.
    # To fix it, I have defined the "total" variable in the function body as the VAT calculation, and moved the
    # function call to its correct place, after the def has run.
    total = amount * 1.2
    # When called, the function will return the "total" value, but as we want to see the result in the console,
    # the print() function is used and there is no return statement.
    print(total)
# The function call now correctly occurs after the def has run.  It has the argument value 100, which is copied
# to the corresponding parameter "amount" inside the function.  So the function now executes total = 100 * 1.2 = 120.0
# It then returns the value of "total", which is 120.0, and prints it.
calculate_vat(100)