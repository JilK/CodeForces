#Code-

n= int(input())
gr= list(map(int, input().split()))
count=0
if 1 not in gr:
    print(0)
else:
    x= gr.count(1)
    y= gr.count(2)
    t= min(y,x)
    x=x-t
    count= t + x//3
    print(count)
