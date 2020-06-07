#Code:

j=0
for i in range(int(input())):

    a = input().split()

    b= int(a[1])
    c= int(a[2])
    if b>=2400 and c>b:
        j=1
        break
if j==1:
    print("YES")
else:
    print("NO")
