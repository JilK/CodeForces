#Code:

a= input().split()
b= int(a[0])
c= int(a[1])
d= int(a[2])
e= int(a[3])
large= max(b,c,d,e)
o=[]
if large>b:
    o.append(large-b)
if large>c:
    o.append(large-c)
if large>d:
    o.append(large-d)
if large>e:
    o.append(large-e)
print(o[0],o[1],o[2])
