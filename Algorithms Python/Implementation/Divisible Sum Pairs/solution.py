#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest_score = scores[0]
    lowest_score = scores[0]
    upper_bound_broken = 0
    lower_bound_broken = 0
    for i in range(len(scores)):
        if scores[i]>highest_score:
            upper_bound_broken+=1
            highest_score = scores[i]
        if scores[i]<lowest_score:
            lower_bound_broken+=1
            lowest_score = scores[i]


    return [str(upper_bound_broken),str(lower_bound_broken)]
if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
