"""只能用于数字"""

List = [1, 3, 6, 3, 2, 2, 3, 4, 5, 4, 6, 7]
if List:
    List.sort(reverse=True)  # 把 List 重新排序，默认是升序
    # list.sort( key=None, reverse=False)
    # key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    # reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
    last = List[-1]
    print(last)  # 打印结果是列表中的最后一个数7
    print(len(List))  # 打印结果是列表的长度12
    for i in range(len(List)-2, -1, -1):  # 在这里，len(List)-2是指列表中的倒数第二个数，-1是指列表中的第一个数，步长是-1表示列表从后往前扫描
        # range(start, stop[, step])
        # start: 计数从 start 开始。默认是从 0 开始。
        # stop: 计数到 stop 结束，但不包括 stop
        # step：步长，默认为1
        if last == List[i]:  # 判断扫描到的值是否与最后一个值相同
            del List[i]  # 如果相同，则将该相同值删除
        else:
            last = List[i]  # 如果列表扫描一遍没有与最后的值相同的值，则将倒数第二的值做为最后的值，重新扫描
    print(List)

    """如何从Python列表中删除重复项"""

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)
"""
从列表中删除重复项
使用“列表”项作为键来创建字典。这将自动删除所有重复项，因为字典不能具有重复键
然后，将字典转换回列表
"""
