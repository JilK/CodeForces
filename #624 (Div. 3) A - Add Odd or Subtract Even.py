#Code- 

for i in range(int(input())):
    a,b=map(int,input().split())
    # print(a,b)
    diff=a-b
    if diff==0:
        print("0")
    elif diff<0:
        if diff%2!=0:
            print("1")
        else:
            print("2")
    elif diff>0:
        if diff%2==0:
            print("1")
        else:
            print("2")
