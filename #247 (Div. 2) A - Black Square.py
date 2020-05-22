#Code:

a=[ int(x) for x in input().split()]
b=input()
c=[]
for i in b:
    i=int(i)
    j=i-1
    c.append(a[j])
    
print(sum(c))
