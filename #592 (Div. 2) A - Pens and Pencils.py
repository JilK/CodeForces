#Code:

import math
for i in range(int(input())):
    a,b,c,d,k= input().split()

    pencil= math.ceil(int(b)/int(d))

    pen= math.ceil(int(a)/int(c))
    if pen+pencil<=int(k):
        print(pen, pencil)
    else:
        print(-1)
