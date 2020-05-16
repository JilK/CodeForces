#Code:

ab= input().split()
a= ab[0]
b= ab[1]
puzzle= [int(1) if int(x)+int(b) <= 5 else int(10) for x in input().split()]
 
count= puzzle.count(1)
teams = count//3
print(teams)
