# 函数可以返回多个值
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c


a, b, c = f()
print(a, b, c)
return_value = f()  # 函数其实只返回了一个对象，也就是一个元组，最后该元组会被拆包到各个结果变量中
print(return_value)  # 这里的return_value将会是一个含有3个返回值的三元元组

"""还有一种非常具有吸引力的多值返回方式——返回字典"""


def f():
    a = 5
    b = 6
    c = 7
    return {'a': a, 'b': b, 'c': c}


return_value = f()
print(return_value)
"""
5 6 7
(5, 6, 7)
{'a': 5, 'b': 6, 'c': 7}
"""
