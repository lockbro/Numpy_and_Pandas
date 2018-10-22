import pandas as pd

# 对文件进行读取:read_文件类型('文件名称')
data = pd.read_csv('test.csv')
# pandas读取完之后会自动加索引
print(data)

# 文件的导出(或者叫保存):to_文件类型('文件名称')
data.to_pickle('test.pickle')
