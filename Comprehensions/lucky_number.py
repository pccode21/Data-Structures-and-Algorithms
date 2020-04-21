values = [3,5,2,7,3,8,1,2,4,8,9,3]
print('幸运数是：', [x for x in set(values) if x == values.count(x)])
