import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# step 2.3.
# Import the dataset from this address
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple = pd.read_csv(url, sep=',')
# print(apple.head())


# step 4.
# Check out the type of the columns
# print(apple.dtypes)


# step 5.
# Transform the Date column as a datetime type
apple.Date = pd.to_datetime(apple.Date)
#print(apple.Date.dtypes)


# step 6.
# Set the date as the index
apple = apple.set_index('Date')
# print(apple.head())


# step 7.
# Is there any duplicate dates?
# print(apple.index.is_unique)


# step 8.
# Make the first entry the oldest date.
# print(apple.sort_index(ascending = True).head(30))


# step 9.
# Get the last business day of each month
apple_month = apple.resample('BM').mean()
# print(apple_month.head())


# step 10.
# What is the difference in days between the first day and the oldest
print((apple.index.max()-apple.index.min()).days)


# step 11.
# How many months in the data we have?
# 
apple_month = apple.resample('BM')
print(len(apple_month.index))