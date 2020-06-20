#Code:

def ans(a):
    count=0
    while a!=1:
        if a%5==0:
            a= (4*a)//5
            count=count+1
        elif a%3==0:
            a= (2*a)//3
            count=count+1
        elif a%2==0:
            a= a//2
            count=count+1
        else:
            break
    if a!=1:
        count=-1

    print(count)


for i in range(int(input())):
    a= int(input())

    ans(a)
