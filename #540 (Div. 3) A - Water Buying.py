#Code:

def ans(n,a,b):

    two_litre= n//2
    remaining= n%2

    if n!=1:
        first_option= two_litre*b + remaining*a
    else:
        first_option= 9999999999999999
    second_option= n*a

    ans= min(first_option , second_option)
    print(ans)


for i in range(int(input())):
    x = input().split()

    n = int(x[0])
    a = int(x[1])
    b = int(x[2])

    ans(n,a,b)
