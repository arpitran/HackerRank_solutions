import numpy as np

n,m = map(int,input().split())
A = np.array([input().split() for _ in range(n)],int)

print(np.min(np.max(A,axis=1)))