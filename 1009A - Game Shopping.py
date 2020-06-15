#Code:

i= input().split()

a=int(i[0])
b=int(i[1])

cost= list(map(int, input().split()))
game= list(map(int, input().split()))

k=0
count=0
j=0
while k<a and j<b:
    if cost[k]<=game[j]:
        count=count+1
        j=j+1
    k=k+1


print(count)
