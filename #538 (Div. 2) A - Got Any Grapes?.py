#Code:

adm = input().split()

a= int(adm[0])
d = int(adm[1])
m = int(adm[2])
tots= a+d+m
gpb = input().split()

g= int(gpb[0])
p= int(gpb[1])
b= int(gpb[2])
total= g+p+b

a= min(g-a, ((g-a)+p)-d,total-tots )

if a>=0:
    print("YES")
else:
    print("NO")
