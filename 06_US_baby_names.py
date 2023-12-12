import pandas as pd
pd.set_option('display.max_columns',None)

#step 2,3,4
#import dataset
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
baby_names = pd.read_csv(url, sep = ',')
#print(baby_names.head(10))

#step 5
#Delete the column 'Unnamed: 0' and 'Id'
#del baby_names['Unnamed: 0']
#del baby_names['Id']
baby_names = baby_names.drop(['Unnamed: 0','Id'], axis = 1)
#print(baby_names.head())


#step 6
#Are there more male or female names in the dataset?
#print(baby_names.Gender.value_counts())


#step 7
#Group the dataset by name and assign to names
#使用iloc篩選出來的是series非dataframe
names = baby_names.groupby('Name').sum()
#print(names.sort_values(['Count'], ascending = False).Count)


#step 8
#How many different names exist in the dataset?
#print(baby_names.Name.value_counts().count())
#print(len(baby_names.groupby('Name').sum()))


#step 9
#What is the name with most occurrences?
#print(names.Count.idxmax())


#step 10
#How many different names have the least occurrences?
#print(len(names[names.Count == names.Count.min()]))


#step 11
#What is the median name occurrence?
#因為先用groupby用Name群組，所以現在name是index，無法用欄篩選出來
me = names[names.Count == names.Count.median()]
#print(me.index)


#step 12
#What is the standard deviation of names?
#print(names.Count.std())


#step 13
#Get a summary with the mean, min, max, std and quartiles.
print(names.Count.describe())