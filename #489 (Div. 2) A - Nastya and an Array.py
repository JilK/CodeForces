#Code - 

n= int(input())

arr= list(set(list(map(int, input().split()))))
if 0 in arr:
    arr.remove(0)
print(len(arr))
