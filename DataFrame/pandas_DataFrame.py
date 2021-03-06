import numpy as np
import pandas as pd

# Series字典
d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
"""
DataFrame是由多种类型的列构成的二维标签数据结构
简单理解是类似于Excel、SQL表的结构
DataFrame支持多种类型的输入数据：
一维ndarray、列表、字典、Series字典；二维numpy.ndarray；结构多维数组或记录多维数组；Series；DataFrame
同Excel一样，DataFrame拥有行标签（index）和列标签（columns），可以理解为Excel的行和列
在构建DataFrame的时候，可以有选择的传递index和columns参数
"""
df = pd.DataFrame(d)
print(df)
"""
字典中使用的两个字符串one和two作为字典的key，在构造DataFrame时会自动的使用字典的key作为自己的columns（列）
输出结果：
   one  two
a  1.0    1
b  2.0    2
c  3.0    3
d  NaN    4
"""
df1 = pd.DataFrame(df, index=['d', 'b', 'c'])
print(df1)
"""
如果在构造DataFrame手动指定索引，那么会使用我们自行指定的索引
输出结果：
   one  two
d  NaN    4
b  2.0    2
c  3.0    3
"""
df2 = pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
print(df2)
"""
如果我们指定的index或者column不存在，将会使用NaN进行默认值填充
输出结果：
   two three
d    4   NaN
b    2   NaN
a    1   NaN
"""
d1 = {'one': [1, 2, 3, 4], 'tow': [4, 3, 2, 1]}
df3 = pd.DataFrame(d1)
# df3 = pd.DataFrame(d1, index=['a', 'b', 'c', 'd'])
print(df3)
"""
多维数组字典构建DataFrame
输出结果：
   one  tow
0    1    4
1    2    3
2    3    2
3    4    1
"""
d2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df4 = pd.DataFrame(d2)
print(df4)
"""
列表字典构建DataFrame
输出结果：
   a   b     c
0  1   2   NaN
1  5  10  20.0
"""
d3 = ({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
       ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
       ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
       ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
       ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
df7 = pd.DataFrame(d3)
print(df7)
"""
元组字典构建DataFrame
元组字典可以创建多层索引DataFrame
输出结果：
       a              b
       b    a    c    a     b
A B  1.0  4.0  5.0  8.0  10.0
  C  2.0  3.0  6.0  7.0   NaN
  D  NaN  NaN  NaN  NaN   9.0
"""
d4 = [{'a': 123, 'b': 1234, 'c': 'cdm'}, {'a': 3222, 'b': 1234, 'c': 'gg'}, {'a': 123, 'b': 1234, 'c': 'cdm'}]
seen = set()  # Python内置函数set()创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
new_d4 = []  # 创建一个空列表
for d in d4:  # 循环执行列表字典d4中的字典，d就是执行后的字典
    t = tuple(sorted(d.items()))
    print(t)
    # Python内置函数tuple()将字典项目转换为元组。
    # Python内置函数sorted()对所有字典项目进行排序操作,reverse = True 降序 ，reverse = False 升序（默认）
    if t not in seen:  # 判断元素集里面是否包含元组 t
        seen.add(t)  # 如果没包含，则添加元组 t 进元素集里面
        new_d4.append(d)  # 将字典追加到新的列表中
print(new_d4, '\n')
df8 = pd.DataFrame(new_d4)
print(df8)
"""
删除列表字典中重复的字典
输出结果：
[{'a': 123, 'b': 1234, 'c': 'cdm'}, {'a': 3222, 'b': 1234, 'c': 'gg'}]

      a     b    c
0   123  1234  cdm
1  3222  1234   gg
"""
df9 = pd.DataFrame(new_d4, index=['one', 'two'])
print(df9)
"""
输出结果：
        a     b    c
one   123  1234  cdm
two  3222  1234   gg
"""
print(df9['a'])  # 按列索引 a 输出
"""
输出结果：
one     123
two    3222
"""
print(df9.loc['one'])  # 按行索引 one 输出
"""
输出结果：
a     123
b    1234
c     cdm
"""
print(df8.iloc[0])  # 按行索引 0 输出
"""
输出结果：
a     123
b    1234
c     cdm
"""
df9['d'] = df9['a'] + df9['b']
print(df9, '\n')
df9['flag'] = df9['a'] > 200
print(df9)
"""
输出结果：
        a     b    c     d
one   123  1234  cdm  1357
two  3222  1234   gg  4456

        a     b    c     d   flag
one   123  1234  cdm  1357  False
two  3222  1234   gg  4456   True
"""
del df9['c']  # 删除数据
print(df9)
df9.pop('flag')  # 删除数据
print(df9)
"""
输出结果：
        a     b     d   flag
one   123  1234  1357  False
two  3222  1234  4456   True
        a     b     d
one   123  1234  1357
two  3222  1234  4456
"""
df9['e'] = '9'  # 插入数据
print(df9)
df9['f'] = df9['a'][:1]  # 插入数据
print(df9)
df9.insert(1, 'bar', df9['a'])  # 插入数据
print(df9)
"""
输出结果：
        a     b     d  e
one   123  1234  1357  9
two  3222  1234  4456  9
        a     b     d  e      f
one   123  1234  1357  9  123.0
two  3222  1234  4456  9    NaN
        a   bar     b     d  e      f
one   123   123  1234  1357  9  123.0
two  3222  3222  1234  4456  9    NaN
"""
# 查看数据
datas = pd.date_range('20200217', periods=6)  # date_range生成时间序列,periods要生成的周期数
print(datas)
df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=list('ABCD'))  # randn(6, 4)随机生成6行4列的数据集
print(df)
"""
输出结果：
DatetimeIndex(['2020-02-17', '2020-02-18', '2020-02-19', '2020-02-20',
               '2020-02-21', '2020-02-22'],
              dtype='datetime64[ns]', freq='D')
                   A         B         C         D
2020-02-17  0.459428  2.113647 -0.818638  0.476076
2020-02-18 -0.470112 -1.082750 -1.265090 -1.566451
2020-02-19 -1.014389 -1.609222  0.414638 -0.483029
2020-02-20  0.651876  0.168563  0.417128 -1.760238
2020-02-21 -0.700649 -0.706482  0.133046  0.248649
2020-02-22 -0.616667  0.600174 -1.218329  0.931850
"""
# 查看头部数据
print(df.head(1))
"""
输出结果：
                   A         B         C         D
2020-02-17 -0.471857  0.666619 -0.006274  1.045691
"""
# 查看尾部数据
print(df.tail(2))
"""
                   A         B         C         D
2020-02-21 -0.717734  1.188148 -2.027126 -1.630341
2020-02-22 -0.515033 -0.141793 -0.350421 -0.035385
"""
# 获取索引
print(df.index)
"""
输出结果：
DatetimeIndex(['2020-02-17', '2020-02-18', '2020-02-19', '2020-02-20',
               '2020-02-21', '2020-02-22'],
              dtype='datetime64[ns]', freq='D')
"""
# 获取列名
print(df.columns)
"""
输出结果：
Index(['A', 'B', 'C', 'D'], dtype='object')
"""
# 查看数据的统计摘要
print(df.describe())
"""
输出结果：
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean  -0.551516 -0.007368  0.166636  0.757952
std    0.854604  1.177190  0.634418  0.551525
min   -1.829759 -1.515879 -0.407782 -0.253618
25%   -1.074763 -0.891489 -0.311242  0.631842
50%   -0.424122  0.034896  0.031681  0.921717
75%    0.126920  0.874759  0.382167  1.135107
max    0.349948  1.447449  1.270793  1.216441
"""
# 转置数据，行列倒换
print(df.T)
"""
输出结果：
   2020-02-17  2020-02-18  2020-02-19  2020-02-20  2020-02-21  2020-02-22
A   -0.042031    1.167181    1.697343   -0.251309   -0.085342    0.502439
B    1.313856    1.098268    1.076856   -0.697947    0.697050    0.329416
C   -2.540740    0.316477   -0.435911   -0.273828   -1.888271    0.198522
D    0.428288    0.099906    0.820917    0.967839    0.413974    0.440377
"""
# 两种排序 sort_index() 和 sort_values()
df1 = pd.DataFrame({'b': [1, 2, 3, 2], 'a': [4, 3, 2, 1], 'c': [1, 3, 8, 2]}, index= [2, 0, 1, 3])
print(df1)
"""
输出结果：
   b  a  c
2  1  4  1
0  2  3  3
1  3  2  8
3  2  1  2
"""
# sort_values() 排序
# 按 b 列升序排序
print(df1.sort_values(by='b'))
"""
输出结果：
   b  a  c
2  1  4  1
0  2  3  3
3  2  1  2
1  3  2  8
"""
# 先按 b 列降序，再按 a 列升序排序
print(df1.sort_values(by=['b', 'a'], axis=0, ascending=[False, True]))
# ascending默认是True升序，False降序
# axis{0 or ‘index’, 1 or ‘columns’}, default 0
"""
输出结果：
    b  a  c
1  3  2  8
3  2  1  2
0  2  3  3
2  1  4  1
 """
# 按行 3 升序排列,必须指定 axis = 1
print(df1.sort_values(by=3, axis=1))
"""
输出结果：
   a  b  c
2  4  1  1
0  3  2  3
1  2  3  8
3  1  2  2
"""
# 按行 3 升序，行 0 降排列
print(df1.sort_values(by=[3, 0], axis=1, ascending=[True, False]))
"""
输出结果：
   a  c  b
2  4  1  1
0  3  3  2
1  2  8  3
3  1  2  2
"""
