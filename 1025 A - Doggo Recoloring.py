#Code:

n= int(input())
s= str(input())
if len(s)==1:
    print("YES")
else:
    k=0
    for i in s:
        if s.count(i)>=2:
            k=1
            break
    if k==0:
        print("NO")
    else:
        print("YES")
    
