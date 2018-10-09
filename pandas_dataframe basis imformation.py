import numpy as np
import pandas as pd

# DataFrame就相当于np里面的二维数组或者矩阵，
# 我们可以直接用numpy或者导入别的数据来定义DataFrame
# 他可以让我们自己定义行和列的元素索引，默认情况下都是0~N-1的数字
dates = pd.date_range('20181009', periods=7)
# 建立一个7行5列的装满随机值矩阵并定义行和列的索引
df = pd.DataFrame(np.random.randn(7, 5),
                  index=dates,
                  columns=['a', 'b', 'c', 'd', 'e'])

print(df)

# 我们还能加入一个字典来定义这个DataFrame
df1 = pd.DataFrame({'A': 1,  # 为了和后面的对应位置会自动复制到这一列的所有行
                    'B': pd.Timestamp('20181009'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df1)

# 我们可以看DataFrame每一列的数据类型
print(df1.dtypes)

# 获得DataFrame的行索引
print(df1.index)

# 获得DataFrame的列索引
print(df1.columns)

# 获得DataFrame的值
print(df1.values)

# 可以用这个功能来得到这个DataFrame的信息
# 只会显示出里面包含数字的列的信息，里面日期、字符串之类的都不会包含进去
df1.describe()

# 转置
print(df1.T)

# 索引排序,axis可以指定是按照行（1）索引还是列索引（0）来排序
# 还能设置ascending是正序（默认，Ture）还是倒叙（False）
df1.sort_index(axis=1, ascending=False)

# 值排序
# 指定某一行进行排序
df1.sort_values(by='E')
