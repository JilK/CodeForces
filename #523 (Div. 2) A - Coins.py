#Code:

ab= input().split()

a= int(ab[0])
b= int(ab[1])

c=b//a
d=c
if b%a!=0:
    d=c+1
print(d)
