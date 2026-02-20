# Simple lambda
x = lambda a: a + 10
print(x(5))


# Lambda with two arguments
x = lambda a, b: a * b
print(x(5, 6))


# Lambda with three arguments
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# Lambda inside another function
def myfunc(n):
    return lambda a: a * n


# Function that always doubles the number
mydoubler = myfunc(2)
print(mydoubler(11))
