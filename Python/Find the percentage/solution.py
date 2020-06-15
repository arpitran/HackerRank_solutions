if __name__ =='__main__':
    n = int(input("Enter number of students "))
    student_marks = {}
    for _ in range(n):
        name,*line = input("Enter name with scores separated by space").split()
        scores = list(map(float,line))
        student_marks[name]=scores
    query_name = input("Enter the student's name whose % you would like to retrieve ")

    x = round(sum(student_marks[query_name])/len(student_marks[query_name]),2)

    print('%.2f'%x)