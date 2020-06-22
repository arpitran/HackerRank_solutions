import math
import os
import random
import re

def gradingStudents(grades):
    res = []
    for i in range(len(grades)):
        if grades[i]<38:
            res.append(grades[i])
        elif math.ceil(grades[i]/5)*5-grades[i]<3:
            res.append(math.ceil(grades[i]/5)*5)
        else:
            res.append(grades[i])
    return res

if __name__=='__main__':
    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)