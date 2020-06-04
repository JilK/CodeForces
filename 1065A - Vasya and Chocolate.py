#Code:

for i in range(int(input())):

    abcd= input().split()

    a= int(abcd[0])
    b= int(abcd[1])
    c= int(abcd[2])
    d= int(abcd[3])

    e= a//d
    f=0
    if e>=b:
        f= e//b
    total= e + f*c
    print(total)
