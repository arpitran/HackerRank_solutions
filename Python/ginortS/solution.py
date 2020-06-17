#!/bin/python3

S = input("Enter a string").strip()
order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
print(*sorted(S,key=order.index),sep="")