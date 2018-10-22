import numpy as np
import pandas as pd

# 制造DF
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
df4 = pd.DataFrame(np.ones((3, 4)) * 3, columns=['b', 'c', 'd', 'e'])

# 上下合并，左右合并(被合并的DF的形式一样的情况)，
# 使用concat方法，axis设为0，对行进行操作，设为1对列操作
# ignore_index为True的时候表示忽律掉合并之前的DF的index
# ignore_index为False的时候表示合并的时候还是保留之前DF的index(默认)
res_axis0 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
res_axis1 = pd.concat([df1, df2, df3], axis=1, ignore_index=True)

# 上下合并(被合并的DF的形式不一样的情况)
# 还是用concat，但是要用我们的参数join来返回不同的结果
# join设为outer(默认情况)直接合并，空的地方用nan填补
res_join = pd.concat([df3, df4], join='outer', ignore_index=True)
print(res_join)
# join设为inner的时候，只会使用各df相同部分合并(取交集)
res_join_inner = pd.concat([df3, df4], join='inner', ignore_index=True)
print(res_join_inner)

# 左右合并(在矩阵形式不一样的时候,可能索引不同)
df5 = pd.DataFrame(np.ones((3, 4)) * 0,
                   columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df6 = pd.DataFrame(np.ones((3, 4)) * 2,
                   columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
# 要是这两个df左右合并的话索引会出现冲突,没有的部分全是NAN
res_not_axes = pd.concat([df5, df6], axis=1)
# 所以我们可加一个join_axes参数，说明以哪一个df的index为主
# 没有的部分再用NAN填充
res_axes = pd.concat([df5, df6], axis=1, join_axes=[df6.index])

# 添加操作append，
# 在pd中就是相当于上下的合并concat，只不过要给一个被加的pd,把后面的pd加在后面
# 我们可以直接追加pd
res_append_pd = df1.append([df2, df3, df2], ignore_index=True)
# 当然也可以只添加一个Series
s_test = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res_append_series = df2.append(s_test, ignore_index=True)
