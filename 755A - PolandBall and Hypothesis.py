#Code:

n= int(input())

k=0
m=0
while k!=1:
    m=m+1
    x= n*m +1
    for i in range(2,x):
        if x%i==0:
            k=1
            break

print(m)
