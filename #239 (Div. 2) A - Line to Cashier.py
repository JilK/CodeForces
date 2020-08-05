#Code:

c = int(input())
q= list(map(int, input().split()))
j=[]
s=0
ans=999999999999999999
for i in range(c):
    j= [int(x)*5 for x in input().split()]
    s= sum(j)+ len(j)*15
    ans= min(ans,s)
print(ans)
