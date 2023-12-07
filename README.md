# pandas-exercises
<br/>

## 1. GitHub 參考指令
| 目標 | 指令 | 說明 |
| --- | --- | --- |
| 其他 | git clone `xxx`<br/>git status||
| 加入索引 | git add `檔案名稱`<br/>git add .|加入單一檔案(推薦)<br/>加入全部檔案|
| 提交版本(給本地數據庫) | git commit -m "`備註說明`" ||
| 上傳遠端數據庫 | git push ||
| 下載遠端數據庫 | git pull||
<br/>

## 2. Pandas 參考寫法
### 寫在最前面
| 目標 | 指令 | 說明 |
| --- | --- | --- |
|| import numpy as np ||
|| import pandas as pd ||
|| pd.set_option('display.max_columns', None) | 顯示完整的欄位資訊 |

### 其他指令
| 目標 | 指令 | 說明 |
| --- | --- | --- |
| 匯入數據 | pd.read_csv(`url`, sep = `'\t'`) ||
| 取頭尾 | head() <br/> tail()||
| 取資訊 | info()||
|| describe() ||
|| dtype | 顯示格式 |
|| columns | 顯示所有欄名稱 |
|| index | 顯示所有index名稱 |
|| [`指定欄的名稱`] ||
| 群組 | groupby(`欄位名稱`)||
| 計算 | sum()||
|| count() |統計數量|
|| nunique()|統計不重複數量|
|| value_counts()|統計不同項目的分別數量|
|| sort_values([`計算的欄位`], ascending = `False`) | value_counts()並排序|
