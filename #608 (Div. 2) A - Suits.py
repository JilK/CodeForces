#Code:

tie = int(input())
scarf= int(input())
vest= int(input())
jacket= int(input())
cost1= int(input())
cost2= int(input())

a= min(tie,jacket)
b= min(scarf,vest,jacket)
if cost2>=cost1:
    jacket=jacket-b
    c= min(tie,jacket)
    ans= cost1*c + cost2*b

else:
    jacket= jacket-a
    c= min(scarf,vest,jacket)
    ans= cost2*c + cost1*a

print(ans)
