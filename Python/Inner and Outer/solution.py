import numpy as np

A = np.array([list(map(int,input().split()))])
B = np.array([list(map(int,input().split()))])

print(np.inner(A,B)[0][0])

print(np.outer(A,B))