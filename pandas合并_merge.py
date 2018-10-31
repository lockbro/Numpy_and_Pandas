import numpy as np
import pandas as pd

# merge方法是可以利用key/keys或者index将两个df合并

# 按照key/keys的方式
# 要是两个矩阵有相同的key的情况
left_0 = pd.DataFrame(
    {'key': ['K0', 'K1', 'K2', 'K3'],
     'A': ['A0', 'A1', 'A2', 'A3'],
     'B': ['B0', 'B1', 'B2', 'B3']})
right_0 = pd.DataFrame(
    {'key': ['K0', 'K1', 'K2', 'K3'],
     'C': ['C0', 'C1', 'C2', 'C3'],
     'D': ['D0', 'D1', 'D2', 'D3']})
# on后面加一个参数(相同的那个key)，表示按照那个key来将两个矩阵连接起来
# 就是只保留两个矩阵都有的key中的一个key
res_0 = pd.merge(left_0, right_0, on='key')

# 要是两个矩阵各有两个不同的key
left_1 = pd.DataFrame(
    {'key1': ['K0', 'K0', 'K1', 'K2'],
     'key2': ['K0', 'K1', 'K0', 'K1'],
     'A': ['A0', 'A1', 'A2', 'A3'],
     'B': ['B0', 'B1', 'B2', 'B3']})
right_1 = pd.DataFrame(
    {'key1': ['K0', 'K1', 'K1', 'K2'],
     'key2': ['K0', 'K0', 'K0', 'K0'],
     'C': ['C0', 'C1', 'C2', 'C3'],
     'D': ['D0', 'D1', 'D2', 'D3']})
# merge默认是用inner的方法(取交集),将key公有的那几行提出来合并
# 要是有一对多的情况也都单独提出来
# 下面两种方法都是等效的
res_1 = pd.merge(left_1, right_1, on=['key1', 'key2'])
res_1_inner = pd.merge(left_1, right_1, how='inner')

# how参数为outer的时候
# 相当于取两个矩阵的合集，没有的部分用nan填补
res_1_outer = pd.merge(left_1, right_1, how='outer')

# how参数为left
# 整个矩阵就基于左边的df来进行填充，先把左边的df整个放进去
# 然后右边的df要是不满足左边的就用nan进行填充
# indicator默认False，要是开了True就是显式的说明merge的方式,我们还能引号自定义那一列的名称
res_1_left = pd.merge(left_1, right_1, how='left', indicator='merge_way')


# merge按照index的方式
left_index_0 = pd.DataFrame(
    {'A': ['A0', 'A1', 'A2'],
     'B': ['B0', 'B1', 'B2']},
    index=['K0', 'K1', 'K2'])

right_index_0 = pd.DataFrame(
    {'C': ['C0', 'C2', 'C3'],
     'D': ['D0', 'D2', 'D3']},
    index=['K0', 'K2', 'K3'])

# 另left_index参数和right_index参数设为True
# 使这个矩阵按照两个df的index进行合并
# 同样还可以设置how来定义合并形式，没有的用nan填充
res_index_outer = pd.merge(left_index_0, right_index_0,
                           left_index=True, right_index=True, how='outer')

# 如何解决重叠问题overlapping
# 用suffixes来区分两个pf中名字相同但是内涵不相同的数据
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'],
                     'age': [1, 2, 3]})

girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'],
                      'age': [4, 5, 6]})
res_suffixes = pd.merge(boys, girls, on='k',
                        suffixes=('_boy', '_girl'), how='inner')
