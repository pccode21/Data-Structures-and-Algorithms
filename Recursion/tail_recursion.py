"""
使用尾递归求 1+2+3+4+5+...+n=(1+n)*n/2 的值
"""
def tail_recursion(n, total=0):
    if n == 0:
        return total
    else:
        return tail_recursion(n-1, total + n)


def main():
    n = int(input('Please input a number:'))
    result = tail_recursion(n, 0)
    print('This number sum is :', result)


if __name__ == '__main__':
    main()
