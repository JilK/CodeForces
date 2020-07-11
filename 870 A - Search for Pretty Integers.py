#Code:

nm= input().split()
first= list(map(int, input().split()))
second= list(map(int, input().split()))
first.sort()
second.sort()
ans=''
a= min(first)

k=0
for i in first:
    if i in second:
        k=1
        ans=i
        break
if k==1:
    print(ans)
else:
    b=min(second)
    if a<b:
        ans= str(a)+str(b)
    else:
        ans=str(b)+str(a)
    print(ans)
