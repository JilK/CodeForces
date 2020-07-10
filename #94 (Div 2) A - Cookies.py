#Code:

n= int(input())
coo= list(map(int, input().split()))
cookie= [int(0) if int(i)%2==0 else int(1) for i in coo]
if sum(coo)%2==0:
    ans= cookie.count(0)
    print(ans)
else:
    ans= cookie.count(1)
    print(ans)
