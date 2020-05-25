#Code:

inp= input()
array= list(map(int, input().split()))
array.sort()
tots=i=0
while i <len(array):
    total= array[i+1]-array[i]
    tots=tots+total
    i=i+2
print(tots)
