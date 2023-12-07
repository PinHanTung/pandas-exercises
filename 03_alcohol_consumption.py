import pandas as pd
pd.set_option('display.max_columns',None)

#step 2.2257
#step 3.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
drinks = pd.read_csv(url, sep = ',')
#print(drinks.head())

#step 4.
#Which continent drinks more beer on average?
#print(drinks.groupby('continent').beer_servings.mean())


#step 5.
#For each continent print the statistics for wine consumption.
#print(drinks.groupby('continent').wine_servings.describe())


#step 6.
#Print the mean alcohol consumption per continent for every column
drinks_select = drinks.iloc[:,1:]
#print(drinks_select.groupby('continent').mean())


#step 7.
#Print the median alcohol consumption per continent for every column
#print(drinks[drinks.dtypes != 'object'])
print(drinks_select.groupby('continent').median())


#step 8.
#Print the mean, min and max values for spirit consumption.
print(drinks.groupby('continent').spirit_servings.agg(['mean','max','min']))