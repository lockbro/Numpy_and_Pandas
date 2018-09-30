###############################################
# array 的创建
#####################################
# 位数越小占用空间越小，别的形式自己查查
import numpy as np

arr1 = np.array(
    [[1, 2, 3],
     [4, 5, 6]], dtype=np.int64)
print(arr1.dtype)

arr2 = np.array(
    [[1, 2, 3],
     [4, 5, 6]], dtype=np.int32)
print(arr1.dtype)

arr3 = np.array(
    [[1, 2, 3],
     [4, 5, 6]], dtype=np.float64)
print(arr1.dtype)

arr4 = np.array(
    [[1, 2, 3],
     [4, 5, 6]], dtype=np.float32)
print(arr1.dtype)

# 全零矩阵
arr5 = np.zeros((4, 5))
print(arr5)

# 全1矩阵
arr6 = np.ones((4, 5), dtype=np.int64)
print(arr6)

# 分配空间，里面是垃圾值
arr7 = np.empty((4, 5))
print(arr7)

# 生成1维的数列, arrage(start, end, interval)
arr8 = np.arange(50, 100, 2)
print(arr8.size)


# 将一维数列转换为矩阵(前提是能恰好分成)
arr9 = np.arange(50, 100, 2).reshape((5, 5))
print(arr9)

# 生成线段linspace(start, end, element_number_in_the_line)
arr10 = np.linspace(1, 10, 5)
print(arr10)

# 将线段转换为矩阵(前提是能恰好分成)
arr11 = np.linspace(1, 10, 6).reshape((2, 3))
print(arr11)