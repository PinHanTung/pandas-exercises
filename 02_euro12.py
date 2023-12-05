import pandas as pd


#step 2.3.
#import dataset
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
euro12 = pd.read_csv(url, sep = ',')
print(euro12)


#step 4.
#select only goal column
#print(euro12['Goals'])


#step 5.
#how many team participated in the Euro2012
#print(euro12.shape[0])


#step 6.
#what is the number of columns un the dataset
#print(euro12.shape[1])


#step 7.
#view only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
#print(discipline)


#step 8.
#sort the teams by Red Cards, then to Yellow Cards
discipline_sort = discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)
print(discipline_sort)


#step 9.
#calculate the mean Yellow Cards given per Team
average = euro12['Yellow Cards'].mean()
print(average)


#step 10.
#filter teams that scored more than 6 goals#not equal
team_filter = euro12[euro12.Goals > 6]
print(team_filter['Team'])


#step 11.
#select the teams that start with G
team_g = euro12[euro12.Team.str.startswith('G')]
print(team_g)


#step 12.
#select the first 7 columns
pd.set_option('display.max_columns',None)
#print(euro12.iloc[:,0:7])


#step 13.
#select all columns except the last 3.
#print(euro12.iloc[:,0:-3])


#step 14.
#Present only the Shooting Accuracy from England, Italy and Russia
#推測team非index，所以沒辦法使用像後面找column名稱的方法，而是使用isin
print(euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']])

