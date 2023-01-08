# QUESTION 2.1:
# Explain what this program does ...
for number in range(100):
    output = 'o' * number
    print(output)

# LINE 3:
# "for" is the keyword, denoting this is a for loop.

# "number" is the loop variable, which takes on the value of the next element in the
# iterable, on each pass through the loop.

# "range(100)" is the iterable, meaning the collection of objects used in interation.
# range(<end>) function returns an iterable that yields integers starting with 0,
# up to, but not including, <end>. So range(100) yields integers starting with 0
# up to, but not including 100.  Therefore, the integers 0-99 will be iterated through.

# LINE 4:
# "output = 'o' * number" is statement 1 of the loop body, and will be executed once
# for each value in the iterable (0-99).  On each execution, the "output" variable
# will be a string consisting of "number" concatenated copies of "o".

# LINE 5:
# "print(output)" is statement 2 of the loop body, and will also be executed once
# for each value in the iterable (0-99). On each execution, the "output" variable
# is printed.

# WHAT THIS PROGRAM DOES:
# Python calls iter() to obtain an iterator for the iterable, range(100).

# Then python calls next() repeatedly to obtain each item from the iterator in turn,
# giving the value of "number" each time.

# In the first pass through the loop: number = 0, so output = o * 0 = " ", so " " is printed.

# In the second pass through the loop: number = 1, so output = o * 1 = "o", so "o" is printed.

# In the third pass through the loop: number = 2, so output = o * 2 = "oo", so "oo" is printed.

# ... and so on ...

# In the final pass through the loop: number = 99, so output = o * 99, so a string of 99 "o" is printed.

# Now all the values from the iterator have been returned, when Python makes a subsequent next() call
# it raises a StopIteration exception. Any further attempts to obtain values from the iterator will fail,
# so the for loop ends.