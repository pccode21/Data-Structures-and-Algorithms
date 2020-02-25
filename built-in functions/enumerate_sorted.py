"""
enumerate函数
当你索引数据时，使用enumerate的一个好方法是计算字典（唯一的）dict映射到位置的值
sorted函数
sorted函数可以从任意序列的元素返回一个新的排好序的列表
"""
some_list = ['foo', 'bar', 'baz']
mapping = {}
# for i, v in enumerate(some_list):
for i, v in enumerate(some_list, start=1):  # 可以设定索引从1开始
    mapping[v] = i
print(mapping)
a = sorted([7, 1, 2, 6, 0, 3, 2])
print(a)
"""
{'foo': 0, 'bar': 1, 'baz': 2}
{'foo': 1, 'bar': 2, 'baz': 3}
[0, 1, 2, 2, 3, 6, 7]
"""
