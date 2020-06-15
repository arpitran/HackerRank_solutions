if __name__ =='__main__':
    n = int(input("Enter number of scores"))
    arr =list(set(map(int,input("Enter space separated list of scores").split())))
    print(sorted(arr,reverse=True)[1])