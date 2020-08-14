#Code;

import math

for i in range(int(input())):
    a,b,c= input().split()
    print(math.ceil(int(c)/2) *int(a) - math.floor(int(c)/2) *int(b))
