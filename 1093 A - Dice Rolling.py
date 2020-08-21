#Code:

for i in range(int(input())):
    x= int(input())
    y= x//7
    if x<=7:
        print(1)
    elif x%7>=2:
        print(y+1)
    else:
        y= x//6
        if x%6==0:
            print(y)
        else:
            print(y+1)
