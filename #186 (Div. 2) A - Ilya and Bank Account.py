#Code:

a= int(input())
if a>=0:
    print(a)
else:
    b=str(a)
    length= len(b)
    d=b[:length-1]
    e= b[:length-2]+b[length-1]
    d=int(d)
    e=int(e)
    if d==0 or e==0:
        print(0)
    elif d>e:
        print(d)
    else:
        print(e)
