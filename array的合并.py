import numpy as np

a = np.array([1, 1, 1])
b = np.array([3, 3, 3])

# 将两个array上下合并：vertical stack
c = np.vstack((a, b))
print(c)
# 将两个array左右合并：horizontal stack
d = np.hstack((a, b))
print(d)
# 如果我们想要a的转置和b的转置左右合并
a_T = a.reshape((3, 1))
b_T = b.reshape((3, 1))
# 因为两个都是一维的数组，直接用.T的方法得到的还是一维数组
# 所以可以用reshape
e = np.hstack((a_T, b_T))
print(e)
# 左右合并还有一种方法就是用newaxis
# 在列的位置新创建一个维度
a_T_New = a[:, np.newaxis]
b_T_New = b[:, np.newaxis]
e_New = np.hstack((a_T_New, b_T_New))
print(e_New)

# 我们可以使用一个更加简洁的方法，就是用concatence
# concatence可以直接定义怎么合并矩阵，只需要指定axis就可以了
# 左右合并
f = np.concatenate((a_T_New, a_T_New, b_T_New, a_T_New), axis=1)
print(f)
# 上下合并
g = np.concatenate((a_T_New, a_T_New, b_T_New, a_T_New), axis=0)
print(g)
