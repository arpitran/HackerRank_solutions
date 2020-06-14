a = int(input("Enter number of elements in set A "))
A = set(map(int,input("# Spaced Separated list of elements of A ").split()))  # Spaced Separated list of elements of A
n = int(input("Number of sets ")) # Number of sets

for i in range(n):
    p = input("Enter the operation and number of elements in set"+i).split()
    s2 = set(map(int,input("Enter space separated list of elements for operation #"+p[1]+" ").split()))
    if p[0] == "intersection_update":
        A.intersection_update(s2)
    elif p[0]=="update":
        A.update(s2)
    elif p[0]=="symmetric_difference_update":
        A.symmetric_difference_update(s2)
    elif p[0]=="difference_update":
        A.difference_update(s2)

print(sum(A))