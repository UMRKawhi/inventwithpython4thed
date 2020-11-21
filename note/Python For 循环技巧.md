# Python For 循环技巧

## 1. 列表

在遍历列表时，有时会想要同时得到列表的index和value。可以使用enumerate函数：

```Python
fam = [1.73, 1.68, 1.71, 1.89]
for index, value in enumerate(fam):
	print(index, value)
```

## 2. 字典

在遍历字典时，可以使用Direction.items()方法同时获得key-value pairs:

```Python
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
for key, value in europe.items():
    print('the capital of {} is {}'.format(key, value))
```

## 3. numpy数组

对于n维numpy数组，需要一次遍历获得里面每一个元素的值可以使用np.nditer()函数，使用时需要import numpy库

```Python
import numpy as np
# np_baseball是一个n维numpy数组
for i in np.nditer(np_baseball):
    print(i)
```

## 4. DataFrame 数据帧

![image-20201121121508762](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201121121508762.png)

```Python
# 使用iterrows()函数遍历DataFrame的每一行
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# lab <- label, row <- row
for lab, row in cars.interrows():
    # lab的结果为US, AUS等，row的输出形式为Series
    print('{}: {}'.format(lab, row['cars_per_cap']))
```

