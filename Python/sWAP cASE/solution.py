#!/bin/python3

def swap_case(s):
    res = []
    for i in range(len(s)):
        if s[i].islower() == True:
            res.append(s[i].upper())
        elif s[i].isupper() == True:
            res.append(s[i].lower())
        elif s[i].islower() == False and s[i].isupper() == False:
            res.append(s[i])
    return ''.join(res)

if __name__=='__main__':
    s = input()
    result = swap_case(s)
    print(result)
    