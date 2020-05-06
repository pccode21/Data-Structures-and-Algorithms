"""
对下面给出的字典按值从大到小对键进行排序
"""
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
sort_price = sorted(prices, key=lambda x: prices[x], reverse=True)
print(sort_price)
"""
输出结果：
['GOOG', 'FB', 'AAPL', 'ACN', 'IBM', 'ORCL', 'SYMC']
"""
