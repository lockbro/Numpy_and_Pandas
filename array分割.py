import numpy as np

a = np.arange(12).reshape((3, 4))
print(a)
# 使用split方法，指定分成几块，
# axis指定怎么分，为1就按行来分割，为0就按列来分割,前提是能等量分割
print(np.split(a, 3, axis=0))
print(np.split(a, 4, axis=1))

# 但如果我们要进行不等量的分割
# 这时候可以用"array_split"这个函数
print(np.array_split(a, (2, 1, 1), axis=1))  # 默认情况
print(np.array_split(a, (1, 2, 1), axis=1))
print(np.array_split(a, (1, 1, 2), axis=1))

# 还有更为简单的方法就是和之前合并的一样
# 纵向分割就是vsplit，横向分割就是hsplit
print(np.vsplit(a, 3))
print(np.hsplit(a, 4))
