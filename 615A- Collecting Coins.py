# Input
# The first line of the input contains one integer t (1≤t≤104) — the number of test cases.

# The next t lines describe test cases. Each test case is given on a new line and consists of four space-separated integers a,b,c and n (1≤a,b,c,n≤108) — the number of coins Alice has, the number of coins Barbara has, the number of coins Cerene has and the number of coins Polycarp has.

# Output
# For each test case, print "YES" if Polycarp can distribute all n coins between his sisters and "NO" otherwise.


#!/bin/python3

import math
import os
import random
import re
import sys
save=[]
# Complete the coin function below.
def coins(p, q, r, s):
    arr=[]
    arr.append(p)
    arr.append(q)
    arr.append(r)
    arr.sort()
    d= (arr[2]-arr[0]) + (arr[2]-arr[1])
    diff=s-d
    if d==s:
        return "YES"
    elif d<s and diff%3==0:
        return "YES"

    else:
        return "NO"


for i in range(int(input())):
  pqrs = input().split()

  p = int(pqrs[0])

  q = int(pqrs[1])

  r = int(pqrs[2])

  s = int(pqrs[3])

  result = coins(p, q, r, s)

  save.append(result)


for i in save:
  print(i,end='\n')