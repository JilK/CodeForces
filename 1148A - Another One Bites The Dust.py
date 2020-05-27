#Code:

pqr= input().split()
p= int(pqr[0])
q= int(pqr[1])
r= int(pqr[2])
s= min(p,q)
total = 2*r + 2*s
if p==q:
    print(total)
else:
    print(total+1)
