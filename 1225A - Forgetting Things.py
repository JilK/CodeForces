#Code:

n= input().split()
a= int(n[0])
b= int(n[1])

diff= a-b
if a==9 and b==1:
    print(9, 10)
elif diff==0:
    ans= str(a)+str(0)+ " "+str(b)+str("1")
    print(ans)
elif diff==-1:
    ans= str(a)+str(9)+ " "+str(b)+str("0")
    print(ans)
else:
    print(-1)
