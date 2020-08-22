#Code :

li=[]
x= int(input())
for i in range(x):
    s= input().split()
    li.append(s)
n= int(input())
i=0
j=0
while i<=len(li)-1:
    if int(li[i][1])>=n:
        ans=i
        break
    i=i+1
print(x- ans)
