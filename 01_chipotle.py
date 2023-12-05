#Step 1.
import numpy as np
import pandas as pd


#Step 2.
#Step 3.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')


#Step 4.
pd.set_option('display.max_columns', None)
#print(chipo.head(10))


#Step 5.
#print(chipo.shape[0])
#print(chipo.info())


#Step 6.
#print(chipo.shape[1])
#print(chipo.info())


#Step 7.
#print(list(chipo.columns))
#print(chipo.columns)


#Step 8.
#print(list(chipo.index))


#Step 9.
#c = chipo.groupby('item_name')
#c = c.sum()
#c = c.sort_values(['quantity'], ascending = False)
#print(c.head(1)['quantity'])


#Step 10.
#u = chipo['item_name'].nunique()
#print(u)


#Step 11.
#c2 = chipo.groupby('choice_description').sum()
#c2 = c2.sort_values(['quantity'], ascending = False)
#print(c2.head(1)['quantity'])


#Step 12.
#t = chipo['quantity'].sum()
#print(t)


#Step 13.
#print(chipo['item_price'].dtype)

dollar = lambda x: float(x[1:])
chipo['item_price'] = chipo['item_price'].apply(dollar)

#print(chipo['item_price'].dtype)


#Step 14.
#r = (chipo['item_price']*chipo['quantity']).sum()
#print(r)


#Step 15.
#cv = chipo['order_id'].value_counts().count()
#print(cv)


#Step 16.
#chipo['revenue'] = chipo['quantity'] * chipo['item_price']
#order_grouped = chipo.groupby(by=['order_id']).sum()
#re = order_grouped['revenue'].mean()
#print(re)


#Step 17.
item_c = chipo['item_name'].value_counts().count()
print(item_c)
