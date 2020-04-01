"""
阶乘函数
递归必须包含一个基本的出口(base case)，否则就会无限递归，最终导致栈溢出。比如这里就是 n == 0 返回 1
递归必须包含一个可以分解的问题(recursive case)。 要想求得 fact(n)，就需要用 n * fact(n-1)
递归必须必须要向着递归出口靠近(toward the base case)。 这里每次递归调用都会 n-1，向着递归出口 n == 0 靠近
"""
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def main():
    n = int(input('Please input a number:'))
    result = fact(n)
    print('This number the factorial result is :', result)


if __name__ == '__main__':
    main()
