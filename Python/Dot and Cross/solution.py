import numpy as np

a = int(input())

arr1 = np.array([list(map(int,input().split())) for _ in range(a)])
arr2 = np.array([list(map(int,input().split())) for _ in range(a)])

print(np.dot(arr1,arr2))