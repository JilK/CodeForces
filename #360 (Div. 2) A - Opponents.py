#Code:

a = input().split()

b= int(a[0])
c= int(a[1])
st=''
li=[]
for i in range(c):
    li.append(1 if b*'1' not in input().split() else 0)


c=0
ma=0

for i in li:

    if i==0:
        c=0
    else:
        c=c+1
        ma= max(ma,c)

print(ma)
