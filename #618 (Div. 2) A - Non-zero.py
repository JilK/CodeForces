#Code:

for i in range(int(input())):
    n= int(input())
    li= list(map(int, input().split()))

    x= li.count(0)
    test=[]
    for i in li:
        if i!=0:
            test.append(i)
        else:
            test.append(1)
    if (sum(test))==0:
        x=x+1
    print(x)
