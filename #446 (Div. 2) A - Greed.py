#Code-
n= int(input())

can = list(map(int, input().split()))

capacity = list(map(int, input().split()))

vol= sum(can)

capacity.sort(reverse=True)
max_capacity = int(capacity[0]) + int(capacity[1])

if vol<=max_capacity:
    print("YES")
else:
    print("NO")
