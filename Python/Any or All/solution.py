#!/bin/python3

class Main():
    def __init__(self):
        self.n = int(input("Enter N"))
        self.li = list(map(int,input("Enter space separated list of N").split()))

    def output(self):
        print(all(i>0 for i in self.li) and any(str(i)==str(i)[::-1] for i in self.li))

if __name__ == "__main__":
    obj = Main()
    obj.output()