import pandas as pd
import numpy as np
pd.set_option('display.max_columns',None)


#step2,3
#import dataset
url1 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv'
url2 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv'
cars1 = pd.read_csv(url1,sep = ',')
cars2 = pd.read_csv(url2,sep = ',')
#print(cars1.head())
#print(cars1.info())
#print(cars2.head())
#print(cars2.info())


#step 4
#delete unamed blank columns
cars1 = cars1.loc[:,'mpg':'car']
#print(cars1.head())
#print(cars1.info())


#step5
#What is the number of observations in each dataset?
#print(cars1.shape)
#print(cars2.shape)


#step6
#Join cars1 and cars2 into a single DataFrame called cars
#append合併方式以被棄用，所以使用concat
cars = pd.concat([cars1,cars2], axis = 0)
# print(cars.shape)


#step7
#Create a random number Series from 15,000 to 73,000.
nr_owners = np.random.randint(15000,high = 73001,size=398,dtype='int')
#print(nr_owners)


#step8
#Add the column owners to cars
cars['owners'] = nr_owners
print(cars.tail())