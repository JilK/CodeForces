#Code:

i= int(input())

test= list(map(int, input().split()))

li=[]
for i in test:
    if i not in li and i!=0:
        li.append(i)

print(len(li))
