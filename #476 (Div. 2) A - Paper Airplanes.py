#Code:

import math
a,b,c,d= input().split()

n= math.ceil(int(b)/int(c))
l= n*int(a)

ans= math.ceil(l/int(d))
print(ans)
