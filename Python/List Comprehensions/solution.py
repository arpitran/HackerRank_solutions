if __name__ ==' __main__':
    x = int(input("Enter X"))
    y = int(input("Enter Y"))
    z = int(input("Enter Z"))
    n = int(input("Enter N"))

    arr = [ [X,y,z] for X in range(x+1) if X !=n]

    print(arr)
