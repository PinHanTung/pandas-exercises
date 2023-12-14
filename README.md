# pandas-exercises
<br/>

## 1. GitHub 參考指令
| 目標 | 指令 | 說明 |
| --- | --- | --- |
| 其他 | git clone `xxx`<br/>git status||
| 加入索引 | git add `檔案名稱`<br/>git add .|加入單一檔案(推薦)<br/>加入全部檔案|
| 取消索引 | git reset `檔案名稱` ||
| 提交版本(給本地數據庫) | git commit -m "`備註說明`" ||
| 上傳遠端數據庫 | git push ||
| 下載遠端數據庫 | git pull||
<br/>

## 2. Pandas 參考寫法
### 寫在最前面
| 目標 | 指令 | 說明 |
| --- | --- | --- |
| np | import numpy as np ||
| pd | import pandas as pd ||
|| pd.set_option('display.max_columns', None) | 顯示完整的欄位資訊 |
| plt | import matplotlib.pyplot as plt | 繪圖使用 |
| sns | import seaborn as sns | 繪圖使用(進階) |


### 其他指令
| 目標 | 指令 | 說明 |
| --- | --- | --- |
| 匯入數據 | pd.read_csv(`url`, sep = `'\t'`, index_col = `欄名稱`) | 從csv匯入數據，index_col可以指定欄為index|
|| pd.DataFrame(`字典名`) | 從字典的數據轉為df |
| 取資訊 | info()| 每欄名稱、數量、格式|
|| describe() | mean、std、min、max、quartiles |
|| shape ||
|| dtypes | 顯示格式，前面可以是df或col |
|| type(`DataFrame名稱`) | 確認格式是否為dataframe |
|| columns | 顯示所有欄名稱 |
|| index | 顯示所有index名稱 |
|| [`欄名稱`] | 選取欄，如果沒有該欄則會新增欄|
|| head() <br/> tail()| 取頭尾 |
| 增減與排列 | del `DataFrame`[`欄名稱`]| 刪除欄，這裡不能使用df.col格式|
|| drop([columns1, columns2], axis = 1) | 刪除欄(可一次多個)|
|| [`欄名稱`] | 選取欄，如果沒有該欄則會新增欄|
|| pd.caoncat([`df1`,`df2`], axis = 0)| 合併dataframe，0為上下合併|
|| `df`=`df`[[col1,col2,col3]] | 指定欄位排列順序 |
|| `df`= `df`.set_index(`col`)| 指定某欄為index(col不會保留)|
|| `df`.index = `df.col` | 指定某欄為index(col會保留)|
| 重新採樣<br/>(加總合併) | resample(`時間`).sum()|時間參考寫法：AS(年初)、10AS(十年)、MS(每月開始)、QS(每季度開始)、YS(每年開始)、W(每周)、D(每天)、H(每小時)|
| 轉換格式(時間) | pd.to_datetime(`DataFrame.欄名稱`, format='%Y')| %Y指年份|
| 篩選 | loc[:,[`df1`,`df2`]] | 複數columns需要一個[]包起來 |
|| `df`[1:11] | 選取2-11列 |
||`df`[`column`].isin(`要篩選的值`) | 在`column`篩選特定值，複數值用[]包起來 |
| 群組 | groupby(`欄名稱`)| `欄名稱`會變成新的 index|
| 計算 | sum()||
|| count() |統計數量|
|| nunique()|統計不重複數量|
|| value_counts()|統計不同項目的分別數量|
|| sort_values([`column`], ascending = `False`) | 依照某欄的值進行排序|
|| std() | 標準差 |
|| idxmax(0)<br/> idxmin | 尋找每行最大最小值對應的index |
| 應用 | value_counts().count() | 計算該欄不同值的數量 |
|| len(groupby(`column`).sum())| 計算該欄不同值的數量 |
|| `df`.index.get_level_values(`index排序或index的名稱`) | 獲取某個index的全部值(使用groupby後可能有不只一個index)|
<br/>

## 3. Numpy 參考寫法
### 有時會和 pandas 一起用
| 目標 | 指令 | 說明 |
| --- | --- | --- |
|| import numpy as np ||
|| np.random.randint(low, high=None, size=None, dtype=int) | 在某個區間值，選擇需要 size 的隨機值|
<br/>

## 4. 繪圖 參考寫法
### 包含 matplotlib.pyplot & seaborn
| 目標 | 指令 | 說明 |
| --- | --- | --- |
| 新增圖1 | `df`[`column`].plot(kind='bar') | 使用`column`數據新增圖 |
|| plt.xlabel(`x軸文字`)<br/> plt.ylabel(`y軸文字`)<br/> plt.title('`標題`')| 圖的文字設定 |
|| plt.show() | 顯示圖片 |
| 新增圖2| sns.FacetGrid(`df`, col=`column`) | 使用`df`數據、按照`column`不同值為主題，產生多個空的圖面 |
|| map(`plt.scatter`,`column_x`,`column_y`,alpha=1)| 為空的圖面填入值，`plt.scatter`為圖形類型，此為散點圖；設定xy值需要的欄，alpha=1為點的透明度|
|| add_legend() | 在圖的旁邊新增圖例 |
|| plt.show() | 顯示圖片 |

