#Code:

x= input().split()

y= int(x[0])
b=int(x[1])
r= int(x[2])
ans=0
minimum= min(y,b,r)
poss=[]
if minimum<=r and b>=r-1 and y>=r-2:
    ans= r+r-1+r-2
    poss.append(ans)
elif minimum<=b and r>=b+1 and y>=b-1:
    ans= b+b-1+b+1
    poss.append(ans)
elif minimum<=y and b>=y+1 and r>=y+2:
    ans= y+y+1+y+2
    poss.append(ans)

print(max(poss))
