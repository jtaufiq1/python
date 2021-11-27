#!/bin/env python3

# Fibonacci Sequence 

a, b = 0, 1

while(a < 1000):
    print(a)
    # print(a, end=',')
    a, b = b, a + b
    
    # a = b
    # b = a + b
print("\n")
