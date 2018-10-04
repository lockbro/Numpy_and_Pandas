import numpy as np

# 一维的情况
a = np.arange(3, 15)
print(a[5])

# 多维的情况
b = np.arange(3, 15).reshape((3, 4))
print(b)
# 索引某个数值，两种表示方法，有一种坐标的感觉,
# 前面代表行，后面代表列
print(b[2][1])
print(b[2, 1])
# 索引某一行
print(b[1, :])
# 索引某一列
print(b[:, 3])
# 索引某个部分(就用切片就可以)
print(b[2, 1:3])
print(b[:2, 3])

# 循环输出
# 循环输出行，默认是循环行
for line in b:
    print(line)
# 循环输出列,因为numpy中没有迭代列的方法，
# 所以我们可以先将矩阵转置再循环行
for column in b.T:
    print(column)


# 循环输出每一项
# flatten方法会返回一个折叠成一维的数组
c = a.flatten()
print(c)
for item in c:
    print(item)
# flat方法会直接返回一个迭代器
for item in b.flat:
    print(item)
