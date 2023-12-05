import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')

pd.set_option('display.max_columns', None)

dollar = lambda x: float(x[1:])
chipo['item_price'] = chipo['item_price'].apply(dollar)



url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
print('原始數據:',url)


print('資料行數：',chipo.shape[0])
print('資料列數：',chipo.shape[1])
print('列的項目：',list(chipo.columns))
print('品項總數：',chipo['quantity'].sum())
print('總訂單數：',chipo['order_id'].value_counts().count())
r = (chipo['item_price']*chipo['quantity']).sum()
print('總收入：$',r)


chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum()
re = order_grouped['revenue'].mean()
print('平均客單價：',re)


print('')
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending = False)
print('最常點的品項與總數：')
print(c.head(1)['quantity'])


print('')
c2 = chipo.groupby('choice_description').sum()
c2 = c2.sort_values(['quantity'], ascending = False)
print('品項描述中，最常出現的內容與總數：')
print(c2.head(1)['quantity'])


#print('前10列預覽：')
#print(chipo.head(10))
