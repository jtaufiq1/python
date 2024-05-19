#!/usr/bin/python3

def calcFactorial(n):
    fact = i = 1
    while i <= n:
        fact = fact * i
        i += 1
    return fact

print(calcFactorial(5))
