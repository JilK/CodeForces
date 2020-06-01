#Code:

abc = input().split()
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])

d= a+b+c
e= 2*(a+b)
g= 2*(a+c)
h= 2*(b+c)

f= min(d,e,g,h)

print(f)
