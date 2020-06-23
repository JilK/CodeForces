#Code:


for i in range(int(input())):
    x= input().split()
    l1= int(x[0])
    r1= int(x[1])
    l2= int(x[2])
    r2= int(x[3])
    if l1!=r2:
        print(l1,r2)
    elif l1!=l2:
        print(l1,l2)
    elif r1!=r2:
        print(r1,r2)
    else:
        print(r1,l2)
