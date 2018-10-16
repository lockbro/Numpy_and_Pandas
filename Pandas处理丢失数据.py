import numpy as np
import pandas as pd

dates = pd.date_range('20181010', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates,
                  columns=['A', 'B', 'C', 'D'])

# 制造缺失值
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan

# 我们可以使用dropna这个方法来去掉带有nan的行或者列
# axis=0表示去除含有nan的行;axis=1表示去除含有nan的列
# how='any'表示'或运算'(只要含有就去除);
# how='all'表示'与运算'(全部都是nan才去除)
print(df.dropna(axis=0, how='any'))

# 我们可以使用fillna来填充nan
print(df.fillna(value=0))

# 检查df是否有nan,要是缺失就返回ture
print(df.isnull())

# 检查举证中是否有缺失，这里相当于检查上一个矩阵中是否有True
# any表示只要有一个元素与==右边的相等就返回True
print(np.any(df.isnull()) == True)
