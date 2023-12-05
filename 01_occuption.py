import pandas as pd

#step 2.3.
users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep = '|', index_col = 'user_id')


#step 4.
#print(users.head(25))


#step 5.
print(users.tail(10))


#step 6.
print(users.shape[0])


#step 7.
print(users.shape[1])


#step 8.
print(users.columns)


#step 9.
print(users.index)


#step 10.
print(users.dtypes)


#step 11.
print(users['occupation'])


#step 12.
#or
#users.occupation.nunique()
print(users['occupation'].value_counts().count())


#step 13.
#value_counts(): includes decending sort
c = users['occupation'].value_counts()
print(c.head(1).index[0])


#step 14.
print(users.describe())


#step 15.
print(users.describe(include = 'all'))


#step 16.
print(users.occupation.describe())


#step 17.
print(users.age.mean())


#step 18.
#head()tail(): without number insides
#for the situation that has several 1st
print(users.age.value_counts(ascending=True).head())
