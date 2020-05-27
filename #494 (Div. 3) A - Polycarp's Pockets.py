#Code:

p= int(input())
array = list(map(int, input().split()))
a= max(array, key = array.count)
b= array.count(a)
print(b)
