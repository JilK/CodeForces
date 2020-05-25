#Code :

inp= input().split()
a=int(inp[0])
b=int(inp[1])
c=int(inp[2])
d=int(inp[3])
e=int(inp[4])
 
f= (a*b) + (2*d)
g= (a*c) + (2*e)
if f<g:
    print("First")
elif g<f:
    print("Second")
else:
    print("Friendship")
