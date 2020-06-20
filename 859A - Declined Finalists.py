#Code:

a = input()

onsite= list(map(int, input().split() ))

ans= max(0, (max(onsite) -25 ))

print(ans)
