n = int(input("Number of integers"))
s = set(map(int, input().split()))

m = int(input("Enter number of operations"))
for i in range(m):
    p=input().split()
    if p[0] == "remove":
        s.remove(int(p[1]))
    elif p[0] == "discard":
        s.discard(int(p[1]))
    else:
        s.pop()

print(sum(list(s)))