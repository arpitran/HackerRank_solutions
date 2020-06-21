#!/bin/python3

import numpy as np

n,m = map(int,input("Enter space separated integers N, M ").split())

a,b = (np.array([input("Enter integers for array ").split() for _ in range(n)], dtype=int) for _ in range(2))

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
