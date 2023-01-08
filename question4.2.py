# QUESTION 4.2:
# I'm setting up my own market stall to sell chocolates.
# I need a basic till to check the prices of different chocolates that I sell.
# I've started the program and included the chocolates and their prices.
# Finish the program by asking the user to input an item and then output its price.
# chocolates = {
#     'white': 1.50,
#     'milk': 1.20,
#     'dark': 1.80,
#     'vegan': 2.00,
# }

# ANSWER:
# Define chocolates dictionary
chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

# Add input() function to gather user choice; make lowercase and remove spaces
item_choice = input('What type of chocolate would you like to buy? ').strip().lower()

# Output price, on condition of having user choice in chocolates dictionary
if item_choice in chocolates:
    print(f'We stock {item_choice} chocolate, it\'s £{chocolates[item_choice]}')

else:
    print(f'Sorry, we don\'t stock {item_choice} chocolate.')
