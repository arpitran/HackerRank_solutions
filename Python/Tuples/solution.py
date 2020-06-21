if __name__=='__main__':
    n = int(input("Enter number of elements in the list "))
    integer_list = map(int,input().split())

    t = tuple(integer_list)
    print(hash(t))
