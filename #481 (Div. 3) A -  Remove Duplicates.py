#Code - 

l= input()

ab= input().split()
test=[]

ab.reverse()

for i in ab:
    if i not in test:
        test.append(i)
 
print(len(test))

test.reverse()
for i in test:
    print(int(i),end=' ')
