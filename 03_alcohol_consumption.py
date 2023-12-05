import pandas as pd

#step 2.2257
#step 3.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
drinks = pd.read_csv(url, sep = ',')
print(drinks.head())

#step 4.
#Which continent drinks more beer on average?
#print(drinks.groupby('continent').beer_servings.mean())


#step 5.
#For each continent print the statistics for wine consumption.
#print(drinks.groupby('continent').wine_servings.describe())


#step 6.
#Print the mean alcohol consumption per continent for every column
#將文字轉換成數字，
#drinks_int = drinks.apply(pd.to_numeric, errors='coerce')
#print(drinks_int.groupby('continent').mean())

print(drinks.groupby('continent').mean())
