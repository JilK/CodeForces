#Code:

m=int(input())
count=0
for i in range(m):
    a= [int(x) for x in input().split()]
    if (a[1]-a[0])>=2:
        count=count+1
print(count)
