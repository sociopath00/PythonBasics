def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))

a = 0
print(a)
b = 1
print(b)
c = 0
while c<100:
    c = a+b
    print(c)
    b = a
    a = c


import numpy as np
print(dir(np))

