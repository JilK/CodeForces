#Code:

m=int(input())
t=[int(x) for x in input().split()]
 
t.sort()
c=''
c= ' '.join([str(elem) for elem in t]) 
print(c)
