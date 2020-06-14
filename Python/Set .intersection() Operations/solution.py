n =int(input("No. of students subscrbed to English newspapers")) # No. of students subscribed to English newspapers
N = set(map(int,input("# Space separated roll numbers of students in 'n'").split())) # Space separated roll numbers of students in 'n'
b = int(input("# Number of students described to French newspapers")) # Number of students described to French newspapers
B = set(map(int,input("# Space separated roll numbers of students in 'b'").split())) # Space separated roll numbers of students in 'b'

print(len(N.intersection(B)))