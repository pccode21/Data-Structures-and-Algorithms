"""
添加和删除元素
可以用append在列表末尾添加元素
insert可以在特定的位置插入元素
insert的逆运算是pop，它移除并返回指定位置的元素
可以用remove去除某个值，remove会先寻找第一个值并除去
如果已经定义了一个列表，用extend方法可以追加多个元素
也可以用del关键字删除值
"""
b = ['foo', 'peekaboo', 'baz']
b.append('dwarf')
print(b)
b.insert(1, 'red')
print(b)
b.pop(2)
print(b)
b.append('foo')
b.remove('foo')
print(b)
b.extend(['car', 'blue', ' price'])
print(b)
del b[6]
print(b)
"""
['foo', 'peekaboo', 'baz', 'dwarf']
['foo', 'red', 'peekaboo', 'baz', 'dwarf']
['foo', 'red', 'baz', 'dwarf']
['red', 'baz', 'dwarf', 'foo']
['red', 'baz', 'dwarf', 'foo', 'car', 'blue', ' price']
['red', 'baz', 'dwarf', 'foo', 'car', 'blue']
"""
