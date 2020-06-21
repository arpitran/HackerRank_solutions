#!/bin/python3

import numpy as np

n,m,p = map(int,input().split())

arrA = np.array([input().strip().split() for _ in range(n)], int)
arrB = np.array([input().strip().split() for _ in range(n)], int)

print(np.concatenate((arrA,arrB),axis=0))