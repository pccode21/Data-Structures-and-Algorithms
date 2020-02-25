"""
以下是将csv文件的行列进行倒换
"""
import pandas as pd

df = pd.read_csv(r".\Data-Structures-and-Algorithms\built-in functions\weather.csv")
data = df.values  # data是数组，直接从文件读出来的数据格式是数组
index1 = list(df.keys())  # 获取原有csv文件的标题，并形成列表
data = list(map(list, zip(*data)))  # map()可以单独列出列表，将数组转换成列表
data = pd.DataFrame(data, index=index1)  # 将data的行列转换
data.to_csv(r'.\Data-Structures-and-Algorithms\built-in functions\weather1.csv', header=0)
