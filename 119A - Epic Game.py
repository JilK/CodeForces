#Code:

import math
a,b,n= input().split()
c=0
while math.gcd(int(a), int(n))<=int(n):
    x= math.gcd(int(a), int(n))
    n=int(n)-x
    c=0
    if math.gcd(int(b),int(n))<=n:
        y= math.gcd(int(b),int(n))
        n=int(n)-y
        c=1
if c==0:
    print(0)
else:
    print(1)
