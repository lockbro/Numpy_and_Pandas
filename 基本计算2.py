import numpy as np

a = np.arange(2, 14).reshape((3, 4))
print(a)
# 最小值的索引
print(np.argmin(a))

# 最大值的索引
print(np.argmax(a))

# 计算整个矩阵的平均值
_sum = np.sum(a)
_ave = _sum / np.size(a)
print(_ave)
# mean这个函数只加目标矩阵是计算平均值的
print(np.mean(a))
print(a.mean())
# 我们也可以只计算行或者列的平均值
print(np.mean(a, axis=1))
print(np.mean(a, axis=0))
# 计算矩阵的中位数，输出的还是矩阵的平均值
# （要求矩阵是逐位增加的）
print(np.median(a))

# 矩阵的累加(每一项都是这一项和前面所有项的总和)
print(np.cumsum(a))

# 矩阵的累差,这个差是左右相邻元素的差，所以四列才会变为3列
print(np.diff(a))

# 对矩阵的每一行进行排序
b = np.arange(14, 2, -1).reshape((3, 4))
print(np.sort(b))

# 矩阵的转置(行变列，列变行)
print(a.T)
print(np.transpose(a))

# clip函数(作用是滤波)， np.clip(a, a_min, a_max, out=None)
# a为一个目标数组；
# a_min为这个数组的最小值，也就是小于这个值的数全使他们等于这个数
#  a_max为这个数组的最大值，也就是大于这个值的数全使他们等于这个数
#  out = b ， 可以把结果放到b这个数组
print(np.clip(a, 4, 7))
