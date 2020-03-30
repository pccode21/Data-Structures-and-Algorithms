"""斐波那契数列生成器"""
sn = int(input('What is the Fibonacci starting number? '))
rn = int(input('How many numbers do you want?'))
a = sn - sn
b = sn
while a < rn:
    print(a, end=' ')
    a, b = b, a+b
