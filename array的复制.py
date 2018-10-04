import numpy as np

# numpy中复制也分浅拷贝和深拷贝

# 普通的直接用“=”将两个数组连接起来的话就是浅拷贝
# 最终这些数组还是会指向一个原数组
a = np.arange(1, 5)

b = a
c = b
print(b)
a[1] = 24
# 这里b和c还是指向指向原数组a
print(a, b, c)

# 那我们想另外创建一个与原数组独立副本，这时候就要用深拷贝了
e = a.copy()
print(a, e)
e[3] = 5454
print(a, e)
