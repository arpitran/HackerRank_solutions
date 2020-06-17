#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input("Enter N and M separated by space ").split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input("Enter line elements ").rstrip().split())))

    k = int(input("Enter element to sort by "))

    sort_arr = sorted(arr, key = lambda x:x[k])

    for row in sort_arr:
        print(*row)
