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
| 取資訊 | info()| 顯示每欄名稱、數量、格式|
|| describe() | 顯示mean、std、min、max、quartiles |
|| shape | 顯示行列數量 |
|| dtypes | 顯示格式，前面可以是df或col |
|| columns | 顯示所有欄名稱 |
|| index | 顯示所有index名稱 |
|| head() <br/> tail()| 取頭尾 |
|| type(`DataFrame名稱`) | 確認格式是否為dataframe |
|| index.is_unique | 確認index是否有重複 |
| 增減與排列 | del `DataFrame`[`欄名稱`]| 刪除欄，這裡不能使用df.col格式|
|| drop([columns1, columns2], axis = 1) | 刪除欄(可一次多個)|
|| [`欄名稱`] | 選取欄，如果沒有該欄則會新增欄|
|| pd.caoncat([`df1`,`df2`], axis = 0)| 合併dataframe，0為上下合併|
|| `df`=`df`[[col1,col2,col3]] | 指定欄位順序 |
|| `df`.columns= [col1,col2,col3] | 指定欄位名稱(取代原本名稱)|
|| `df`= `df`.set_index(`col`)| 指定某欄為index(col不會保留)|
|| `df`.index = `df.col` | 指定某欄為index(col會保留)|
|| sort_values([`column`], ascending = `False`) | 依照某欄的值進行排序|
|| sort_index([`column`], ascending = `False`) | 依照index的值進行排序|
| 轉換格式(時間) | pd.to_datetime(`DataFrame.欄名稱`, format='%Y')| %Y指年份|
|| days | 以日為單位 |
| 篩選 | loc[:,[`df1`,`df2`]] | 複數columns需要一個[]包起來 |
|| `df`[1:11] | 選取2-11列 |
||`df`[`column`].isin(`要篩選的值`) | 在`column`篩選特定值，複數值用[]包起來 |
| 重新採樣 | `df`.resample(`10AS`).sum()| 十年總和，A為年、S為開頭 <br/> [時間參考寫法](<https://blog.csdn.net/qq_44285092/article/details/117638171>)：10AS(十年)、BM(每月最後一個工作天)、MS(每月開始)、QS(每季度開始)、AS(每年開始)、YS(每年開始)、W(每周)、D(每天)、H(每小時)|
|| `df`.resample(`BM`).mean() | 每月最後一天為區間，取平均值，B為工作、M為月|
| 群組 | groupby(`欄名稱`)| `欄名稱`會變成新的 index|
| 計算 | sum()||
|| count() |統計數量|
|| nunique()|統計不重複數量|
|| value_counts()|統計不同項目的分別數量|
|| std() | 標準差 |
|| idxmax(0)<br/> idxmin | 尋找每行最大最小值對應的index |
| 應用 | value_counts().count() | 計算該欄不同值的數量 |
|| len(groupby(`column`).sum())| 計算該欄不同值的數量 |
|| `df`.index.get_level_values(`index排序或index的名稱`) | 獲取某個index的全部值(使用groupby後可能有不只一個index)|
|| `df2` = `df1`.resample(`'BM'`).mean() <br/> len(`df2`.index) | 計算月數(透過日期重新取樣) |
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
| plt設定 | `df`[`column`].plot(kind=`'bar'`,x=`x軸文字`,y=`y軸文字`,title=`名稱`,figsize=(`6,8`) | 使用`column`數據新增圖，[種類參考](<https://yanwei-liu.medium.com/python-%E8%B3%87%E6%96%99%E8%99%95%E7%90%86%E7%AD%86%E8%A8%98-%E4%BA%8C-%E8%A9%A6%E8%A9%A6%E7%9C%8Bseaborn%E5%90%A7-bf9fecdc1905>) |
|| plt.xlabel(`x軸文字`)<br/> plt.ylabel(`y軸文字`)<br/> plt.title('`標題`')| 圖的文字設定 |
|| set_size_inches(13.5,9) | 設定圖片尺寸 |
| plt存檔與顯示 | fig=`df`.plot().get_figure() <br/> fig.savefig(`figure.png`) | 取得圖片 <br/> 保存成png |
|| plt.show() | 顯示圖片 |
| sns設定 | sns.FacetGrid(`df`, col=`column`) | 使用`df`數據、按照`column`不同值為主題，產生多個空的圖面 |
|| map(`plt.scatter`,`column_x`,`column_y`,alpha=1)| 為空的圖面填入值，`plt.scatter`為圖形類型，此為散點圖；設定xy值需要的欄，alpha=1為點的透明度|
|| add_legend() | 在圖的旁邊新增圖例 |
|| plt.show() | 顯示圖片 |

