def tail_recursion(n, total=0):
    if n == 0:
        return total
    else:
        return tail_recursion(n-1, total + n)

def main():
    n = 5
    for i in range(n, -1, -1):
        total = tail_recursion(n-1, total + n)
        print('tail_recursion(%s, %s)' % (i, total))


if __name__ == '__main__':
    main()
