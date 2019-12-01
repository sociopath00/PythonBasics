"""
    @author: Akshay Nevrekar
    @created_on: 30th Nov,2019
    @last_updated_on:
"""


def sum_n(n):
    if n==1:
        return 1
    return n + sum_n(n-1)

print(sum_n(10))


def fibonacci(n):
    if n==1:
        return 1

    if n==0:
        return 0

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
