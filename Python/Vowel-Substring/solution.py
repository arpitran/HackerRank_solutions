#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def isVowel(x):
    if(x=="a" or x=='e' or x=='i' or x=='o' or x=='u'):
        return True
    return False

def vowelcount(x):
    lowercase = x.lower()
    vowel_counts = {}
    
    for vowel in "aeiou":
        count = lowercase.count(vowel)
        vowel_counts[vowel] = count

    counts = vowel_counts.values()
    total_vowels = sum(counts)
    return total_vowels
    


def findSubstring(s, k):
    test_str = s
    count = 0 
    sub_string = {}
    res = [test_str[i: j] for i in range(len(test_str)) for j in range(i+1, len(test_str)+1) if len(test_str[i:j])==k]
    for i in res:
        sub_string[i]=vowelcount(i)

    if sub_string.get(max(sub_string,key=sub_string.get))==0:
        return "Not found!"
    else:
        return str(max(sub_string,key=sub_string.get))
    # Write your code here
