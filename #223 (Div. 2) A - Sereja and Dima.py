#Code :

n= int(input())

li= list(map(int , input().split()))
i=0
s=0
d=0
while li!=[]:
    if li[0]>li[n-1]:
        s= s+li[0]
        del(li[0])
    else:
        s= s+li[n-1]
        del(li[n-1])
    n=n-1
    if li!=[]:
        if li[0]>li[n-1]:
            d= d+li[0]
            del(li[0])
        else:
            d= d+li[n-1]
            del(li[n-1])
        n=n-1   
        
print(s,d)

