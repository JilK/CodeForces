#Code:

i= int(input())

while i%10!=0:
    k= str(i)
    if int(k[-1])<=5:
        i= i-1

    else:
        i= i+1

print(i)
