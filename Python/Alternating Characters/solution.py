#Alternating Characters
""" You are given a string containing characters A and B only. Your task is to change it into a string such that there are no
matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
For example, given the string s = AABAAB, remove an A at position 0 and 4 to make s = ABAB in 2 deletions.

Function Description
Complete the alternating Characters functions in the editor below. It must return an integer representing the number of deletions to make the 
alternating string
"""
import unittest

def alternatingCharacters(s):
    deletions = 0
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            deletions+=1
    return deletions



if __name__ == "__main__":
    string = "AABBAA"
    print(alternatingCharacters(string))



            

