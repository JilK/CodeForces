#Code:

a= int(input())

array = list(map(int, input().split()))

c= min(array)
d= max(array)
s= (d-c)- a+1
print(s)
