#Code:

n= int(input())

test=[]

test.append(n)

for i in test:
    count=0
    j= str(i)
    k= list(j)
    for l in k:
        count= count+int(l)

    if count%4==0:
        print(i)
    else:
        n=n+1
        test.append(n)
