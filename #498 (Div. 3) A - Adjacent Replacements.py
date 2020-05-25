#Code:

inp= input()
array= list(map(int, input().split()))
test=[]
for i in array:
    if i%2==0:
        test.append(i-1)
    else:
        test.append(i)
for j in test:
    print(j,end=" ")
