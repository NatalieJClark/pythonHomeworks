# QUESTION 1.3:
# I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make.
# Write a program to calculate this.
# Assume that a box of eggs contains six eggs and I need four eggs for each omelette,
# but I should be able to easily change these values if I want.
# The output should say something like "You can make 9 omelettes with 6 boxes of eggs".

# ANSWER:
# Define variables (values can be changed)
eggs_per_box = 6
total_boxes = 6
eggs_per_omelette = 4

# Calculate total eggs with multiplication operator
total_eggs = total_boxes * eggs_per_box

# Calculate total omelettes variable with floor division (answer rounded to next smallest whole number)
total_omelettes = total_eggs // eggs_per_omelette

# Define message variable with .format() method string formatting
message = f'You can make {total_omelettes} omelettes with {total_boxes} boxes of eggs'

# Output message variable
print(message)