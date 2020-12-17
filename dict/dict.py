"""
字典
keys和values是字典的键和值的迭代器方法，可以使用list()函数输出结果。虽然键值对没有顺序，这两个方法可以用相同的顺序输出键和值
用update方法可以将一个字典与另一个融合，update方法是原地改变字典，因此任何传递给update的键的旧的值都会被舍弃。
"""
d = {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}
d1 = list(d.keys())
print(d1)
d2 = list(d.values())
print(d2)
d.update({'b': 'foo', 'c': 12})
print(d)
"""
['a', 'b', 7]
['some value', [1, 2, 3, 4], 'an integer']
{'a': 'some value', 'b': 'foo', 7: 'an integer', 'c': 12}
"""
# 用列表创建字典
# 将两个列表配对组合成字典。下面是一种写法:
dict1 = {}
key_list = ['one', 'two', 'three', 'four']
value_list = ['red', 2, 'blue', 'yellow']
for key, value in zip(key_list, value_list):
    dict1[key] = value
print(dict1)
"""
{'one': 'red', 'two': 2, 'three': 'blue', 'four': 'yellow'}
"""
# 使用随机数
dict2 = dict(zip(range(5), reversed(range(5))))
print(dict2)
"""
{0: 4, 1: 3, 2: 2, 3: 1, 4: 0}
"""
# 可以通过首字母，将一个列表中的单词分类
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:  # by_letter 是 by_letter.keys() 的简写
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
print(by_letter)
"""
{'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
"""
# setdefault方法就正是干这个的。前面的for循环可以改写为
by_letter1 = {}
for word in words:
    letter = word[0]
    by_letter1.setdefault(letter, []).append(word)
print(by_letter1)
"""
{'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
"""
# collections模块有一个很有用的类，defaultdict，它可以进一步简化上面。传递类型或函数以生成每个位置的默认值：
from collections import defaultdict
by_letter2 = defaultdict(list)
for word in words:
    by_letter2[word[0]].append(word)
print(dict(by_letter2))  # 要使用dict()将列表转换成字典
"""
{'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
"""

dic1 = {'1': 'india','2': 'america','3': 'china'}
dic2 = {'A1':'india','A2':'india' ,'A3':'america','A4':'india' ,'A5': 'china','A6': 'india','A7': 'america' }
tmp = {v: k for k, v in dic1.items()}
tmp
dic3 = defaultdict(list)
for k, v in dic2.items():
    dic3[tmp[v]].append(k)
dic3 = dict(dic3)
dic3
"""
{'1': ['A1', 'A2', 'A4', 'A6'], '2': ['A3', 'A7'], '3': ['A5']}
"""
