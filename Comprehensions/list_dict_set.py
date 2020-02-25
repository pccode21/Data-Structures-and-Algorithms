# 列表、集合和字典推导式
a_list = ['a', 2, 'as', 'bat', 5, 'car', 'dove', 3, 'python']
squared_ints = [e**2 for e in a_list if isinstance(e, int)]  # 获取序列中所有整数的列表，然后对它们求平方
"""
e**2 输出表达式
for e in a_list 遍历变量e是否在列表里面
if isinstance(e, int) 谓词检查成员是否为整数
"""
print(squared_ints)
"""
[4, 25, 9]
"""
# 使用内置函数，map, filter和匿名lambda函数可以实现几乎相同的结果
squared_ints = list(map(lambda e: e**2, filter(lambda e: isinstance(e, int), a_list)))
print(squared_ints)
"""
[4, 25, 9]
"""
strings = list(filter(lambda s: isinstance(s, str), a_list))  # 从列表中过滤掉非字符串，将提取的字符串存入列表
upper_strings = [x.upper() for x in strings if len(x) > 2]  # 从新列表中获取长度在2以上的字符串，并将其转换成大写
print(upper_strings)
"""
['BAT', 'CAR', 'DOVE', 'PYTHON']
"""
# 用相似的方法，还可以推导集合和字典。字典的推导式如下所示
# 集合的推导式与列表很像，只不过用的是尖括号
lengths = {len(x) for x in strings}
print(lengths)
# map函数可以进一步简化：
lengths1 = set(map(len, strings))
print(lengths1)
"""
{1, 2, 3, 4, 6}
{1, 2, 3, 4, 6}
"""
# 作为一个字典推导式的例子，我们可以创建一个字符串的查找映射表以确定它在列表中的位置
loc_mapping = {val: index for index, val in enumerate(strings)}
print(loc_mapping)
"""
{'a': 0, 'as': 1, 'bat': 2, 'car': 3, 'dove': 4, 'python': 5}
"""
# 嵌套列表推导式
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
# 用一个列表包含所有的名字，这些名字中包含两个或更多的e。可以用for循环来做：
names_list = []
for names in all_data:
    new_data = [name for name in names if name.count('e') >= 2]
    names_list.extend(new_data)
print(names_list)
# 可以用嵌套列表推导式的方法，将这些写在一起，如下所示：
# 列表推导式的for部分是根据嵌套的顺序，过滤条件还是放在最后
result = [name for names in all_data for name in names if name.count('e') >= 2]
print(result)
"""
['Steven']
['Steven']
"""
# 将一个整数元组的列表扁平化成了一个整数列表
datas = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_datas = [x for data in datas for x in data]
print(new_datas)
"""
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
# 将上面的整数元组的列表转换成一个列表的列表
new_datas1 = [[x for x in data] for data in datas]
print(new_datas1)
"""
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
