#Code-
a,t= input().split()
t= int(t)

b=[abs(86400-int(x)) for x in input().split()]

c=0
s=0
i=0
while s<t:
    s=s+b[i]
    i=i+1
    c=c+1
print(c)
