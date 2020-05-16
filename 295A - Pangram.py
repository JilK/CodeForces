#Code

total=0
n= int(input())
a= str(input())
a=a.lower()
b=''
for i in a:
    if i not in b:
        b=b + i
 
if len(b)==26:
    print("YES")
else:
    print("NO")
