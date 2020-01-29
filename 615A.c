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