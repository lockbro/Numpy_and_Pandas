###############################################
# array 的基础运算
###############################################
import numpy as np

a = np.array([10, 20, 30, 40, 50, 60])
b = np.arange(6)

# 加法
_add = a + b
print("a + b = " + _add)

# 减法
_minus = a - b
print("a - b = " + _minus)

# 数组乘法 (注意 ， 这里只是简单地数组间对应值相互乘而已)
_multiply = a * b
print("a * b = " + _multiply)

# 次方运算·
_power = a ** 4
print("a^4 =  " + _power)

# sin() or cos() or tan()
_sin = 10 * np.sin(a)
_cos = 10 * np.cos(b)
_tan = 10 * np.tan(a)
print(_sin)
print(_cos)
print(_tan)

# 一般对于数组里面的比较大小的运算，都会以布尔值的形式返回
print(a)
print(a < 40)
print(a == 10)

# 矩阵的乘法 np.dot(c, d) != c*d
c = np.array([[1, 2],
              [3, 4]])
d = np.arange(4).reshape((2, 2))
_dot = np.dot(c, d)
# 因为c也是一个np类型的，所以可以换一种表达方式
_dot_other_way = c.dot(d)
print(_dot)
print(_dot_other_way)

# 求最大最小值，还有和
e = np.random.random((2, 4))
print(e)
# 求矩阵中所有元素的和
print(np.sum(e))
# 求矩阵中所有元素中最小的值
print(np.min(e))
# 求矩阵中所有元素中最大的值
print(np.max(e))
# 轴用来为超过一维的数组定义的属性，
# 二维数据拥有两个轴：第0轴沿着行的垂直往下，第1轴沿着列的方向水平延伸。
# 求矩阵所有行和的值
print(np.sum(e, axis=1))
# 求矩阵所有列和的值
print(np.sum(e, axis=0))
# 求矩阵所有行的最小值
print(np.min(e, axis=1))
# 求矩阵所有列的最大值
print(np.max(e, axis=0))
