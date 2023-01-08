# QUESTION 3.1:
# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

# ANSWER:
is_raining = input("Is it raining? (y/n) ").strip().lower()

if is_raining == "y" or is_raining == "yes":
    print("Take an umbrella")
else:
    print("You don\'t need an umbrella")