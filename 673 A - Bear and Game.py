#Code:

n= int(input())

mi = list(map(int, input().split()))

mi.insert(0,0)
ans=0
i=0
try:
    while mi[i+1]-mi[i]<=15:
        ans= mi[i+1]
        i=i+1
    print(ans+15)
except:
    if mi[-1]+15>=90:
        print(90)
    else:
        print(mi[-1]+15)
