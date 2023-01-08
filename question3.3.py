# QUESTION 3.3:
# Your friend works for an antique book shop that sells books between 1800 and 1950 and
# wants to quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872) and outputs the century and decade
# (e.g. "Eighteenth Century, Seventies")

# ANSWER:
# Ask year
year = input("What year was the book written? (YYYY) ")

# List of numbers as words
num_words = ["Six", "Seven", "Eight", "Nine"]

# Categorise century
if 1800 <= int(year) <= 1899:
    the_century = "Nineteenth Century"
elif 1900 <= int(year) <= 1950:
    the_century = "Twentieth Century"
# Add condition for books outside age range that shop sells
else:
    the_century = "We don\'t sell books this age"

# Categorise decade
if 1800 <= int(year) <= 1950:
    if year[2] == "0":
        dec_written = "Noughties"
    elif year[2] == "1":
        dec_written = "Tens"
    elif year[2] == "2":
        dec_written = "Twenties"
    elif year[2] == "3":
        dec_written = "Thirties"
    elif year[2] == "4":
        dec_written = "Forties"
    elif year[2] == "5":
        dec_written = "Fifties"
    else:
        dec_written = f"{num_words[int(year[2])-6]}ties"
else:
    dec_written = "sorry!"

# Print categories
print(f'{the_century}, {dec_written}')
