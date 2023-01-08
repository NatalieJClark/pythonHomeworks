# QUESTION 5.2:
# This program should save my data to a file, but it doesn't work when I run it.
# What is the problem and how do I fix it?
# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'r') as poem_file:
#     poem_file.write(poem)

# ANSWER:
# Create poem.txt file in same folder as Python file
# Open poem.txt file in write mode by changing the open() function second positional
# argument, mode, from 'r' which is read-only mode, to 'w+' parameter.
poem = 'I like Python and I am not very good at poems'

with open('poem.txt', 'w+') as poem_file:
    poem_file.write(poem)
