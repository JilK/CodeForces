#Code :

d={}
d={'purple':'Power', 'green':'Time', 'blue':'Space', 'orange':'Soul','red':'Reality', 'yellow':'Mind'}

n= int(input())
s=''
for i in range(n):
    x= str(input())
    if x not in s:
        s=s+ x +" "
l=[]
for i in d:
    if i not in s:
        l.append(d[i])
print(len(l))
for i in l:
    print(i,end="\n")
