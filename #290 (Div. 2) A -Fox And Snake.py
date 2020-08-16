# Code:

a,b = input().split()
a= int(a)
b= int(b)
x=1
c=0
while x!=a+1:
    if x%2!=0:
        print(b*'#')
    else:
        if c==0:
            print((b-1)*'.'+ 1*'#')
            c=1
        else:
            print(1*'#'+ (b-1) *'.')
            c=0
    x=x+1

