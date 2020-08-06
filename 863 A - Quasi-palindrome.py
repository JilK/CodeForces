#Code:

c = str(input())
x= len(c)-len(c.rstrip('0'))
c= x*'0'+c

l=len(c)


if len(c)%2!=0:

    j= c[: l//2]

    k= c[l//2+1:]
    k=k[::-1]

else:
    j= c[: l//2]

    k= c[l//2:]
    k=k[::-1]

if j==k:
    print("YES")
else:
    print("NO")
