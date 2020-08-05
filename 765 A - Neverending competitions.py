#Code:

c = int(input())
s= str(input())
t=''
for i in range(c):
    t=t+str(input())

x= t.count(s)
if x%2==0:
    print("home")
else:
    print("contest")
