# Python函数都是对象
import re

states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
            'south   carolina##', 'West virginia? ']


def clean_strings1(strings):
    result = []
    for value in strings:
        value = str.strip(value)  # 等同于 value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = str.title(value)  # 等同于 value = value.title()
        result.append(value)
    return result


""" 也可以使用以下多函数模式使你能在很高的层次上轻松修改字符串的转换方式。此时的clean_strings也更具可复用性！："""


def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
    # sub是substitute的所写，表示替换
    # 使用正则表达式 re.sub() 将列表中的 !#? 这些符号代替掉
    # 其中 [] 表示匹配字符集合中的一个字符


clean_ops = [str.strip, remove_punctuation, str.title]  # 将需要在一组给定字符串上执行的所有运算做成一个列表
# strip() 内置函数用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
# title() 内置函数返回"标题化"的字符串,就是说所有单词的首个字母转化为大写，其余字母均为小写


def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


if __name__ == '__main__':
    new_states1 = clean_strings1(states)
    print(new_states1)
    new_states = clean_strings(states, clean_ops)
    print(new_states)
"""
['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South   Carolina', 'West Virginia']
['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South   Carolina', 'West Virginia']
"""
