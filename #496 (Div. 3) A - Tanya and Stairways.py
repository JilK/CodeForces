#Code;

n= int(input())

li= list(map(int, input().split()))

i=0
c=[]
while i<len(li)-1:
    if li[i]>=li[i+1]:
        c.append(li[i])
    i=i+1
x=li[-1]
c.append(x)
print(len(c))
for i in c:
    print(i, end=" ")
