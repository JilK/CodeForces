#Code:

a= int(input())

first= list(map(int,input().split()))
second= list(map(int,input().split()))


pile1= sum(first)
pile2=sum(second)

if pile1>=pile2:
    print("YES")
else:
    print("NO")

