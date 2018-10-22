import numpy as np
import pandas as pd

dates = pd.date_range('20181010', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates,
                  columns=['A', 'B', 'C', 'D'])

# 选择哪些列
# 通过标签进行选择
print(df['A'])
print(df.A)

# 选择哪些行
# 通过切片进行选择
# 哪一行到哪一行
print(df[0:3])
# 也可以用列的标签
print(df['20181011':'20181014'])

# 根据某个索引进行选择 使用loc这个方法
# 根据行标签
print(df.loc['20181013'])
# 根据列标签(前提时所有行都要用切片“:”选上)
print(df.loc[:, ['A', 'B']])
# 同时根据行和列进行选择
print(df.loc['20181011', ['A', 'D']])
print(df.loc['20181012':'20181014', ['B', 'C']])

# 根据位置来进行选择，相当于numpy的坐标，用iloc这个方法
# 但是这个坐标是从0开始计数
# 某一行的数据
print(df.iloc[0])
# 某一行的某一个元素
print(df.iloc[4, 3])
# 进行切片筛选(先行后列)
print(df.iloc[2:, 1:3])
# 可以自行选择行进行筛选
print(df.iloc[[0, 2, 3, 5], 1:3])
print(df.iloc[[0, 2, 3, 5], [0, 3]])

# 可以用一些逻辑运算来筛选
# 虽然我们只对某一列进行了运算筛选，
# 但是pandas还是会筛选掉整个DataFrame中满足条件的东西
print(df[df.B > 10])
print(df[df.A < 5])
