# Pandas是專門為編寫Python的外部模組，主要執行數據處理跟分析。
# Panda由Panel、DataFame、Serise組成

import pandas as pd
import numpy as np
print(pd.__version__)

# Series
# 一種一維陣列資料結構，陣列中可以存放整數、浮點數、字串、Python物件（例如list、dict）、純量...等。
# Series的資料是由一個index或稱為label搭配一個實際的資料，所以看起來會像是一個二維陣列資料。

#使用lists
s = pd.Series([11,12,13,14,15,16])
print('使用lists',s,'\n')

#使用dict
s1 = pd.Series({'台灣':'Taiwan','日本':'Tokyo','韓國':'Korea'})
print('使用dict',s1,'\n')

#使用Numpy的ndarray
s2=pd.Series(np.arange(1,2,5))#產生從1到(2-5)之間序列數字，每次增加5
print('使用Numpy的ndarray',s2,'\n')