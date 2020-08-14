#Code:

m=0
c=0
for i in range(int(input())):
    a,b= input().split()
    if int(a)>int(b):
        m=m+1
    if int(b)>int(a):
        c=c+1
if m>c:
    print("Mishka")
elif c>m:
    print("Chris")
else:
    print("Friendship is magic!^^")
