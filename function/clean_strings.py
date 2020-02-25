import re

states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
            'south   carolina##', 'West virginia? ']


def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
    # sub是substitute的所写，表示替换
    # 使用正则表达式 re.sub() 将列表中的 !#? 这些符号代替掉


clean_ops = [str.strip, remove_punctuation, str.title]
# strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
# title() 方法返回"标题化"的字符串,就是说所有单词的首个字母转化为大写，其余字母均为小写


def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


if __name__ == '__main__':
    new_states = clean_strings(states, clean_ops)
    print(new_states)
