# 对字典进行迭代可以得到其所有的键和值
some_dict = {'a': 1, 'b': 2, 'c': 3}
keys = []
values = []
for key in some_dict:
    keys.append(key)
    values.append(some_dict[key])
print(keys)
print(values)
"""
['a', 'b', 'c']
[1, 2, 3]
"""
# 当你编写for key in some_dict时，Python解释器首先会尝试从some_dict创建一个迭代器
# 迭代器是一种特殊对象，它可以在诸如for循环之类的上下文中向Python解释器输送对象。
# 大部分能接受列表之类的对象的方法也都可以接受任何可迭代对象。比如min、max、sum等内置方法以及list、tuple、set等类型构造器
dict_iterator = iter(some_dict)
print(list(dict_iterator))  # 列表
"""['a', 'b', 'c']"""
# print(tuple(dict_iterator))  # 元组
# print(set(dict_iterator))  # 集合
"""
生成器（generator）是构造新的可迭代对象的一种简单方式。
一般的函数执行之后只会返回单个值，而生成器则是以延迟的方式返回一个值序列，即每返回一个值之后暂停，直到下一个值被请求时再继续。
要创建一个生成器，只需将函数中的return替换为yield即可：
直到从该生成器中请求元素时，它才会开始执行其代码
"""


def squires(n=10):
    print('Generating squares from 1 to {0}'.format(n**2))
    for i in range(1, n+1):
        yield i**2


gen = squires()
for i in gen:
    print(i, end=' ')
print('\n')
"""
Generating squares from 1 to 100
1 4 9 16 25 36 49 64 81 100
"""
# 另一种更简洁的构造生成器的方法是使用生成器表达式（generator expression）。
# 这是一种类似于列表、字典、集合推导式的生成器。其创建方式为，把列表推导式两端的方括号改成圆括号
gen = (x**2 for x in range(1, 11))
print(list(gen))
"""[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] """
# 生成器表达式也可以取代列表推导式，作为函数参数：
s = sum(x**2 for x in range(1, 11))
print(s)
"""385"""
d = dict((i, i**2) for i in range(1, 5))
print(d)
"""{1: 1, 2: 4, 3: 9, 4: 16}"""
