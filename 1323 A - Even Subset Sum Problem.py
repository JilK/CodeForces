#Code:

for i in range(int(input())):
    n= int(input())
    a= list(map(int,input().split()))
    k=0

    for i in a:
        if i%2==0:
            k=i
            break

    if k!=0:
        print(1)
        print(a.index(k)+1)
    else:
        if len(a)==1:
            print(-1)
        else:
            print(2)
            print(1,2)
    
