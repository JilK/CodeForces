#Code :

abcd = input().split()

a= int(abcd[0])
b=int(abcd[1])
c=int(abcd[2])
d=int(abcd[3])

if a+b==c+d or a+c==b+d or a+d==b+c or a+b+c==d or b+c+d==a or c+d+a==b or d+a+b==c:
    print("YES")
else:
    print("NO")
