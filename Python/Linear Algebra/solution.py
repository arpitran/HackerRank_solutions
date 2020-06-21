#!/bin/python3

import numpy as np
np.set_printoptions(legacy='1.13')

n = int(input())
a = np.array([input().split() for _ in range(n)], float)
print(round(np.linalg.det(a)))
