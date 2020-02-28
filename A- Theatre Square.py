'''
Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

Input
The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).

Output
Write the needed number of flagstones.

'''

import math
import os
import random
import re
import sys
 
# Complete the function below.
 
def fun(p,q,r):
    b=0
    a= p//r
    c=q//r
    if p%r!=0:
        a=a+1
    if q%r!=0:
        c=c+1
    b=a*c
    print(int(b))
 
 
pqrs = input().split()
 
p = int(pqrs[0])
 
q = int(pqrs[1])
 
r = int(pqrs[2])
result = fun(p, q, r)