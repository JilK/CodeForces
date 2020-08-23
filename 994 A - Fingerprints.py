# Code :

a,b = input().split()

li= list(map(int, input().split()))
test= list(map(int, input().split()))

ans=[]
for i in li:
    if i in test:
        ans.append(i)

for i in ans:
    print(i, end=" ")
