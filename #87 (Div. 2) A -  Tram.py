#Code:

left=0
enter=0
ans=0
total=0
array= []
for i in range(int(input())):
    ab= input().split()
    a= int(ab[0])
    b= int(ab[1])
    left= total - a
    enter = b
    total = enter + left
    array.append(total)
print(max(array))
