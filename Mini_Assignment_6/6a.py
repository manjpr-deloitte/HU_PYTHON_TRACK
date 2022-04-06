def twice(func):
    def inner(num1,num2):
        func(num1,num2)
        func(num1,num2)
    return inner
@twice
def multiply(n1, n2):
    print(n1 * n2)
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
multiply(n1, n2)
