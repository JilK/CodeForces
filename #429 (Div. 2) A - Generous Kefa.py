#Code-

mn= input().split()
n= int(mn[1])
s= str(input())
k=0
for i in s:
    if s.count(i)>n:
        k=2
        break
if k==0:
    print("YES")
else:
    print("NO")
