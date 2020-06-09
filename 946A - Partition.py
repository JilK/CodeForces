#Code:

i= int(input())

test= list(map(int, input().split()))
b=[]
c=[]
for i in test:
    if i>0:
        b.append(i)
    else:
        c.append(i)

print(sum(b)-sum(c))
