import numpy as np

np.set_printoptions(legacy='1.13')

n,m = map(int,input().split())
arr = np.array([input().split() for _ in range(n)],int)

print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(np.std(arr,axis=None))