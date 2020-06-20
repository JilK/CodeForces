#Code:

a = input().split()

x= int(a[0])
y=int(a[1])
z= int(a[2])
t1= int(a[3])
t2= int(a[4])
t3= int(a[5])

stairs= abs(x-y) * t1

elevator= abs(z-x)*t2 + 2*t3 + abs(x-y)*t2 + t3
if stairs>=elevator:
    print("YES")
else:
    print("NO")
