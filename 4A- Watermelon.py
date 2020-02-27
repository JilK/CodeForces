#!/bin/python3
 
import math
import os
import random
import re
import sys
 
# Complete the function below.
 
def fun(p):
    if p%2==0 and p>2:
        print("YES")
    else:
        print("NO")
 
 
p= int(input())
 
result = fun(p)