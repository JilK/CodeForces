#Code:

a= str(input())

n= a.count('n')
i=a.count('i')
e= a.count('e')
t=a.count('t')

n=n-3
extra= 1
n=n//2 + extra
i=i
e=e//3
t=t
if min(n,i,e,t)<0:
    ans=0
else:
    ans= min(n,i,e,t)

print(ans)
