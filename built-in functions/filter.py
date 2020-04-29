"""
filter是用于过滤的高阶函数
filter(function, sequence)
filter() 函数的功能：对 sequence 中的 item 依次执行 function(item)，
将结果为 True 的 item 组成一个 List/String/Tuple（取决于 sequence 的类型）并返回。
"""
selected_numbers = filter(lambda x: x % 3 == 0, range(1, 11))
print(list(selected_numbers))

s = list(filter(lambda x: x%2==0, range(10)))
print(s)
"""使用列表推导式替换如下："""
s = [x for x in range(10) if x%2==0]
print(s)
