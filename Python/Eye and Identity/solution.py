#!/bin/python3

import numpy as np

n,m = map(int,input("Enter shape of your array ").split())

print(str(np.eye(n,m,k=0)).replace('1',' 1').replace('0',' 0'))

