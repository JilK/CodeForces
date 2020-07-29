#Code:

x=[]
y=[]

for i in range(int(input())):
    point= input().split()
    x.append(int(point[0]))
    y.append(int(point[1]))

minus=0
plus=0
for i in x:
    if i<0:
        minus=minus+1
    else:
        plus=plus+1

if minus<=1 or plus<=1:
    print("Yes")
else:
    print("No")
