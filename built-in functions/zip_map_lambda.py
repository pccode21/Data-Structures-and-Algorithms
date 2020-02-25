"""
zip(seqa, [seqb, [...]])
zip（）接受一个或多个序列并将它们按列的元素编织在一起，当最短的顺序用完时，编织停止。
list(zip())返回一个真实的Python列表[]。
"""
# 例子：
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = (9, 10, 11)
d = (12, 13)
print(list(zip(a, b)))
# 输出：[(1, 5), (2, 6), (3, 7), (4, 8)]
print(list(zip(a, d)))
# 输出：[(1, 12), (2, 13)]
print(list(zip(a, b, c, d)))
# 输出：[(1, 5, 9, 12), (2, 6, 10, 13)]

"""
请注意，当序列长度相同时，zip（）是可逆的：
"""
# 例子：
a = (1, 2, 3)
b = (4, 5, 6)
x = zip(a, b)
print(list(zip(a, b)))
# 输出：[(1, 4), (2, 5), (3, 6)]
y = zip(*x)  # 或者, apply(zip, x)
print(list(y))
# 输出：[(1, 2, 3), (4, 5, 6)]
z = zip(*zip(*zip(a, b)))  # 或者, apply(zip, y)
print(list(z))
# 输出：[(1, 4), (2, 5), (3, 6)]
print(list(x) == list(z))
# 输出：True

"""
map(function, iterable, ...)
function -- 函数
iterable -- 一个或多个序列
map() 会根据提供的函数对指定序列做映射。
返回迭代器
"""
def square(x):  # 计算平方数
    return x**2
sq1 = map(square, [1, 2, 3])  # 计算列表各个元素的平方
print(list(sq1))
sq2 = map(lambda x: x**2, [1, 2, 3, 4])  # 使用 lambda 匿名函数
print(list(sq2))
sq3 = map(lambda x, y: x + y, [1, 2, 3, 4], [2, 3, 4, 5])  # 提供了两个列表，对相同位置的列表数据进行相加
print(list(sq3))
