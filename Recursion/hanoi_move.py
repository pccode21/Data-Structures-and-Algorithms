"""
汉诺塔
解法的基本思想是递归。假设有 A、B、C 三个塔，A 塔有 N 块盘，目标是把这些盘全部移到 C 塔。
那么先把 A 塔顶部的 N-1 块盘移动到 B 塔，
再把 A 塔剩下的大盘移到 C，
最后把 B 塔的 N-1 块盘移到 C。
如此递归地使用下去, 就可以求解。
"""
def hanoi(n, a, b, c):
    if n == 1:
        print('Move %s --> %s' % (a, c))
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)

def main():
    hanoi(3, 'A', 'B', 'C')


if __name__ == '__main__':
    main()
