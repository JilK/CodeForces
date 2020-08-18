Code:

n= int(input())

s= str(input())

x= s.split("W")
ans=''
c=0
for i in x:
    if len(i)>=1:
        ans= ans+ str(len(i)) +" "
        c=c+1
print(c)
print(ans)
