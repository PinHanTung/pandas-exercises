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
| 匯入數據 | pd.read_csv(`url`, sep = `'\t'`, index_col = `欄名稱`) | index_col可以指定欄為index|
| 重新採樣<br/>(加總合併) | resample(`時間`).sum()|時間參考寫法：AS(年初)、10AS(十年)、MS(每月開始)、QS(每季度開始)、YS(每年開始)、W(每周)、D(每天)、H(每小時)|
| 轉換格式(時間) | pd.to_datetime(`DataFrame.欄名稱`, format='%Y')| %Y指年份|
| 取資訊 | info()||
|| describe() ||
|| shape ||
|| dtype | 顯示格式 |
|| type(`DataFrame名稱`) | 確認格式是否為dataframe |
|| columns | 顯示所有欄名稱 |
|| index | 顯示所有index名稱 |
|| [`欄名稱`] | 選取欄，如果沒有該欄則會新增欄|
|| head() <br/> tail()| 取頭尾 |
| 增減 | del `DataFrame`[`欄名稱`]| 刪除欄|
|| [`欄名稱`] | 選取欄，如果沒有該欄則會新增欄|
|| pd.caoncat([`df1`,`df2`], axis = 0)| 合併dataframe，0為上下合併|
| 群組 | groupby(`欄名稱`)||
| 計算 | sum()||
|| count() |統計數量|
|| nunique()|統計不重複數量|
|| value_counts()|統計不同項目的分別數量|
|| sort_values([`計算的欄位`], ascending = `False`) | value_counts()並排序|
|| idxmax(0) | 尋找每行最大值對應的index |


## 3. Numpy 參考寫法
### 有時會和 pandas 一起用
| 目標 | 指令 | 說明 |
| --- | --- | --- |
|| np.random.randint(low, high=None, size=None, dtype=int) | 在某個區間值，選擇需要 size 的隨機值|
