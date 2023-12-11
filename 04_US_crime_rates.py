import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

#step 2,3,4
#import the dataset
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'
crime = pd.read_csv(url, sep = ',')
#print(crime.head())
#print(crime.info())


#step 5
#convert the type of the column Year to datetime64
crime.Year = pd.to_datetime(crime.Year, format='%Y')
print(crime.info())


#step 6
#Set the Year column as the index of the dataframe
#也可以在匯入資料時進行：pd.read_csv(url, index_col=欄名稱)
#set_index()可以更改index，而reset_index()則可以換回來
#drop = True為預設，刪除要做為新索引的欄位
crime = crime.set_index('Year')
#print(crime.head())


#step 7
#Delete the Total column
del crime['Total']
print(crime.head())


#step 8
#Group the year by dacades and sum the values
#由於人口是長期累積的數、並非每年累加，因此取十年內的最大值，而非加總
crimes = crime.resample('10AS').sum()
population = crime['Population'].resample('10AS').max()
crimes['Population'] = population
print(crimes)
