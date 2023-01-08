# QUESTION 3.2:
# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit.
# I've written a program to check that I can afford the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong
#
# my_money = input('How much money do you have? ')
# boatcost=20+5
#
# if my_money < boat_cost:
#   print('You can afford the boat hire')
# else:
#   print('You cannot afford the board hire')

# ANSWER:
# Add float() function to convert input string into an float, and specify pounds (£)
my_money = float(input("How much money do you have? (£) "))
# Add missing underscore to variable name and turn values into floats
boat_cost = 20.0 + 5.0
# Change comparison operator from less than (<) to greater than or equal to (>=)
if my_money >= boat_cost:
    print("You can afford the boat hire")
else:
    print("You cannot afford the board hire")