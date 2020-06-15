if __name__ =='__main__':
    students = []
    check = set()
    output = []

    for i in range(int(input("Enter number of student "))):
        name = input("Enter Students name ")
        score = float(input("Enter Students score "))
        students.append([name,score])
        check.add(score)

    second_last = sorted(list(check))[1]

    output = [i[0] for i in students if i[1]==second_last]
    output = sorted(output)

    for i in output:
         print(i)
