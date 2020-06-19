#Code:

a = int(input())

c=0
while a>0:
    a=a-1
    c=c+1
    a=a-2
    c=c+1
if a<0:
    print(c-1)
else:
    print(c)
