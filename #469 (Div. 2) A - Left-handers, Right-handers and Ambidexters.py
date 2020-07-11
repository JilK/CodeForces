#Code:

abcd= input().split()
l= int(abcd[0])
r= int(abcd[1])
a= int(abcd[2])

diff=abs(l-r)
if l<r:
    x= min(l+a,r)
    if r==x:
        a=a-diff
        ans= 2*r + 2*(a//2)
    else:
        ans= x*2
elif r<l:
    y= min(r+a,l)
    if l==y:
        a=a-diff
        ans= 2*l + 2*(a//2)
    else:
        ans=2*y
elif l==r:
    ans= 2*l + 2*(a//2)

print(ans)
