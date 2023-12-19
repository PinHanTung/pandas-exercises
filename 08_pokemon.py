import pandas as pd
pd.set_option('display.max_columns',None)

# step 2.3.
# Create a data dictionary
# Assign it to a variable called pokemon
raw_data = {'name':['Bulbasaur','Charmander','Squirtle','Caterpie'],
            'evolution':['Ivysaur','Charmeleon','Wartortle','Metapod'],
            'type':['grass','fire','water','bug'],
            'hp':[45,39,44,45],
            'pokedex':['yes','no','yes','no']}
pokemon = pd.DataFrame(raw_data)
#print(pokemon.head())


# step 4.
# Place the order of the columns as name, type, hp, evolution, pokedex
pokemon = pokemon[['name','type','hp','evolution','pokedex']]
#print(pokemon)


# step 5.
# Add another column called place, and insert what you have in mind.
pokemon['place'] = ['park','street','lake','forest']
print(pokemon)


# step 6.
# Present the type of each column
print(pokemon.dtypes)