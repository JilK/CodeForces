#Code :

import statistics 
for i in range(int(input())):
    a,b= input().split()
    li= list(map(int, input().split()))
    x= statistics.mean(li)
    y= int(b)/len(li)
    if y<=x:
        print(int(b))
    else:
        while y>x:
            b=int(b)-1
            y= int(b)/len(li)
        print(int(b))
