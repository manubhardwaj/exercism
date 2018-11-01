#!/usr/bin/env python3

def fib(n):
    if n < 3:
        return n-2

    return fib(n-1) + fib(n-2)

print(fib(3))
print(fib(4))
print(fib(5))
