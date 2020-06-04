#Code:

abc= input().split()

a= int(abc[0])
b= int(abc[1])
c= int(abc[2])

d= c//a
e=c//b
test=[]
test2=[]
count=0
for i in range(1,d+1):
    test.append(i*a)

for i in range(1,e+1):
    if i*b in test:
        count=count+1

print(count)
