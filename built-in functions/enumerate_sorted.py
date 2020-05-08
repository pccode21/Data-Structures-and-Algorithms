"""
enumerate函数
当你索引数据时，使用enumerate的一个好方法是计算字典（唯一的）dict映射到位置的值
sorted函数
sorted函数可以从任意序列的元素返回一个新的排好序的列表
"""
some_list = ['foo', 'bar', 'baz']
mapping = {}
# for i, v in enumerate(some_list):
for i, v in enumerate(some_list[::-1], start=1):  # 可以设定索引从1开始
    mapping[v] = i
print(mapping)
a = sorted([7, 1, 2, 6, 0, 3, 2])
print(a)
s = ["1bd", "5s", "354d", "4ghds"]
s1 = sorted(s, key=lambda x: x[0])  # 按列表中每个元素的[0]位排序
print(s1)
s2 = sorted(s, key=len)  # 按每个元素的长度排序
print(s2)
a = [[2,3],[4,1],(2,8),(2,1),(3,4)]
b = sorted(a,key=lambda x: (x[0], x[1]))
c = sorted(a,key=lambda x: (x[0], -x[1]))
print(b, '\n', c)
"""
{'foo': 0, 'bar': 1, 'baz': 2}
{'foo': 1, 'bar': 2, 'baz': 3}
[0, 1, 2, 2, 3, 6, 7]
['1bd', '354d', '4ghds', '5s']
['5s', '1bd', '354d', '4ghds']
[(2, 1), [2, 3], (2, 8), (3, 4), [4, 1]]
 [(2, 8), [2, 3], (2, 1), (3, 4), [4, 1]]
"""
