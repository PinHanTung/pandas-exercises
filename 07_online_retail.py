import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="ticks")
pd.set_option('display.max_columns', None)


#step 2,3
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv'
online_rt = pd.read_csv(url, sep = ',', encoding = 'latin1')
#print(online_rt.head())


# step 4
# Create a histogram with the 10 countries that have the most 'Quantity' ordered except UK
# step 1-1, groupby 'Country', and sum quantity
# step 1-2, sort_values by decending
# step 1-3, ？how to ordered except UK
# step 2-1, create the plot
# step 2-2, set the title and labels
# step 2-3, show the plot
se_country = online_rt.loc[:,['Quantity', 'Country']]
se_country = se_country.groupby('Country').sum()
so_country = se_country.sort_values('Quantity', ascending = False)[1:11]

so_country['Quantity'].plot(kind='bar')
plt.xlabel('Countries')
plt.ylabel('Quantity')
plt.title('10 Countries with most orders')
#plt.show()


# step 5
# Exclude negative Quantity entries
online_rt = online_rt[online_rt.Quantity >= 0]
#print(online_rt.head())


# step 6
# Create a scatterplot with the Quantity per UnitPrice by CustomerID for the top 3 Countries (except UK)
# step 1-1,select datasets we need
unitprice = online_rt.loc[:,['Country', 'CustomerID','UnitPrice','Quantity']]
# step 1-2, groupby 'CustomerID','Country', these two columns change into indexs
# step 1-3, sum() and filt UnitPrice>0
unitprice = unitprice.groupby(['CustomerID','Country']).sum()
unitprice = unitprice[unitprice.UnitPrice > 0]
# step 2, change 'Country' from index to column
# info: create a column named 'Country'
# info: get the index values 'Country', then assigned into new column
unitprice['Country'] = unitprice.index.get_level_values('Country')
# step 3, filter df by three top countries(result from step4 )
top_countries = ['Netherlands', 'EIRE', 'Germany']
unitprice = unitprice[unitprice['Country'].isin(top_countries)]
# step 4, create FacetGrids by df=unitprice
g = sns.FacetGrid(unitprice, col='Country')
g.map(plt.scatter, 'Quantity', 'UnitPrice', alpha=1)
#g.add_legend()
plt.show()
