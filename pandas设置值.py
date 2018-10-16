import numpy as np
import pandas as pd

dates = pd.date_range('20181010', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates,
                  columns=['A', 'B', 'C', 'D'])

# 修改df里面的值
# 我们可以用iloc先定位之后修改被定位的目标的值
df.iloc[2, 1] = 11

# 也可以用loc来定位修改值
df.loc['20181015', 'C'] = 44


# 我们也可以使用一些逻辑运算符对一大片值进行修改
# 只对某一列赋值
# (df.A)[df.A > 8] 前面括号选出A列，后面就是选择A的哪些行
df.A[df.A > 8] = 1
# (df.C)[df.B > 13] 前面括号选出C列, 后面就是选B的哪些行，然后对到C列修改
df.C[df.B > 13] = 0

# 对所有列的特定行赋值
# 内部先确定选中的行，也就是>9的行数，外层就是将这些行都赋值
df[df.B > 9] = 0

# 加一列,这里是加了个序列，对应着前面的index
df['F'] = pd.Series([6, 5, 4, 3, 2, 1],
                    index=pd.date_range('20181010', periods=6))
# 先加一列占个位，之后再慢慢赋值
df['E'] = np.NAN
