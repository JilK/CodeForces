#Code:

pqr = input().split()
p = int(pqr[0])
q = int(pqr[1])
r = int(pqr[2])

s = max(p,q,r)
t = min(p,q,r)
u = (p+q+r) - s -t

total = (s-u)+(u-t)
print(total)
