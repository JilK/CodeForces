#Code:

import re

ab= input().split()
a=int(ab[0])
b=int(ab[1])
comment=[]
command=[]
for i in range(a):
    comment.append(str(input()).replace(" ","-"))

for i in range(b):
    command.append(str(input()).replace(" ","-"))
ans=''
for i in command:
    y= i.split('-')[1]
    y=y[:-1]
    for j in comment:
        x=j.split('-')[1]
        if x==y:
            ans= ans+ "\n" + str(i).replace("-", " ") + " #"+str(j.split('-')[0])

print(ans.strip())
