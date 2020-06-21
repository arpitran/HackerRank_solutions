#!/bin/python3

import numpy as np

nums = tuple(map(int,input("Enter shape of your array ").split()))

print(np.zeros((nums),dtype=np.int))

print(np.ones((nums),dtype=np.int))