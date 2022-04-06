def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a, b = b, a + b
n=int(input())
for x in fib(n):
    print(x)