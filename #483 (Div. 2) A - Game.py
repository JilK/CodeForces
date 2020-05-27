#Code- 

p= int(input())
array = list(map(int, input().split()))
array.sort()
q=p//2
if p%2!=0:
    print(array[q])
else:
    print(array[q-1])
