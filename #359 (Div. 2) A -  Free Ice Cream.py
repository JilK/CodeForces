#Code:

a = (input()).split()
k=int(a[0])
l=int(a[1])
s=''
d=0
for i in range(k):
    j= str(input())
    if j.startswith("+"):
        l= l+ int(j[1:])
    else:
        if int(j[1:])<=l:
            l=l-int(j[1:])
        else:
            d=d+1
print(l,d)
