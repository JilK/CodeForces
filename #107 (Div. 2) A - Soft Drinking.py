#Code:

x= input().split()

n= int(x[0])
k= int(x[1])
l= int(x[2])
c= int(x[3])
d= int(x[4])
p= int(x[5])
nl= int(x[6])
np= int(x[7])

ml= k*l
toast= ml//nl
limes= c*d
salt= p//np

number= min(toast,limes,salt)
ans= number//n

print(ans)
