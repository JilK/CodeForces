#Code:

test=[]

for i in range(int(input())+1):
    test.append(int(input()))
size= test[0]
test.remove(test[0])
test.sort(reverse=True)
c=0
n=0
while c<size:
    a= test[0]
    c=c+a
    n=n+1
    test.remove(test[0])

print(n)
