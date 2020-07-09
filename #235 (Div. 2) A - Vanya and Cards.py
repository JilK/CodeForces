#Code:

import math

ab= input().split()

a=int(ab[0])
b= int(ab[1])

cards= list(map(int, input().split()))

ans = abs(sum(cards))//b
extra= abs(sum(cards))%b
extra= math.ceil(extra/b)
print(ans+extra)
