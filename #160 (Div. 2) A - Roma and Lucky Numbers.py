#Code:

a = input().split()

b= int(a[0])
c= int(a[1])
s= input().split()
d=0
for i in s:
    i = str(i)
    if i.count('4')+i.count('7')>c:
        d=d+1

r= b-d
print(r)

