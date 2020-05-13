'''
Input
The input contains three integers a, b and c, each on a single line (1 ≤ a, b, c ≤ 10).

Output
Print the maximum value of the expression that you can obtain.
'''

#!/bin/python3
 
# Complete the code below.
a= int(input())
b= int(input())
c= int(input())
 
d= a+b+c
e= (a+b) * c
f = a* (b+c)
 
h= a*b*c
array=[]
array.append(d)
array.append(e)
array.append(f)
 
array.append(h)
 
print(max(array))
