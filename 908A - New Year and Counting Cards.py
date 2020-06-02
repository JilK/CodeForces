#Code:

ab = str(input())

test= 'aeiou13579'
c=0
for i in ab:
    if i in test:
        c=c+1
print(c)

