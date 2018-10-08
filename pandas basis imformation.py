# import numpy as np
import pandas as pd

# 通过数组创建一个Series
# 与np的区别就是可以创建一个索引,可以看成是定长的有序数列
# nan代表not a number，算是留空
# 这个有点像np的一维数组
# 一般以float数据类型保存数据
# 后面参数可以让我们自己定义索引，默认情况下是0~N-1的数字
a = pd.Series([2, 2, 3, 6, 7], index=['a', 'b', 'c', 'd', 'e'])

print(a)

# 获取索引
print(a.index)

# 获取值
print(a.values)

# 访问值
print(a['a'])
print(a['e'])
print(a[['a', 'c', 'd', 'e']])

# 通过字典创建一个Series
dic = {'Banana': 12, 'Apple': 54, 'Watermelon': 3}
b = pd.Series(dic)
print(b)
# 这个索引相当于字典中的“键”
# 下面相当于用新的index去匹配原有的index，要是匹配的上就显示，匹配不上就出现 NAN与他对应
inde = ['a', 'Banana', 'Apple']
c = pd.Series(dic, index=inde)
print(c)
