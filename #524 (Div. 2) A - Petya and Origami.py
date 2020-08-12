#Code;

import math
a,b = input().split()

blue= int(a)*8
green= int(a)*5
red= int(a)*2

need= math.ceil(blue/int(b)) + math.ceil(green/int(b)) + math.ceil(red/int(b))
print(need)
