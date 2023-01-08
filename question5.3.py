# QUESTION 5.3:
# In this session you used the Pokemon API to retrieve a single Pokemon.
# I want a program that can retrieve multiple Pokemon and save their names and moves to a file.
# Use a list to store about 6 Pokemon IDs.
# Then in a for loop call the API to retrieve the data for each Pokemon.
# Save their names and moves into a file called 'pokemon.txt'

# ANSWER:
# Install requests library using pip.
import requests

# List of Pokemon IDs.
pokemon_id = [10, 25, 54, 125, 5, 7]

# Open pokemon.txt file in write mode.
with open('pokemon.txt', 'w+') as pokemon_file:
    # Loop through list of Pokemon IDs, using API to get the name and move data for each ID,
    # and write data to pokemon.txt file.
    for number in pokemon_id:
        url = f'https://pokeapi.co/api/v2/pokemon/{number}/'
        response = requests.get(url)
        print(response)
        pokemon = response.json()
        pokemon_name = pokemon['name']
        pokemon_file.write(f'\n{pokemon_name}:\n')
        print(pokemon_name)

        moves = pokemon['moves']
        for move in moves:
            pokemon_move = move['move']['name']
            pokemon_file.write(f'{pokemon_move}\n')
            print(pokemon_move)



