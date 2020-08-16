#Code :

s= [x for x in input().split()]

ans=[]
for i in s:
    if i not in ans:
        ans.append(i)
print(4-len(ans))
