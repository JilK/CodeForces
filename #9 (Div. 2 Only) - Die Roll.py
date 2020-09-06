#Code:

a,b=input().split()
c= max(int(a), int(b))
d=6-c+1
if d==2:
    print('1/3')
elif d==3:
    print('1/2')
elif d==6:
    print('1/1')
elif d==4:
    print('2/3')
else:
    print(str(d) +"/"+"6")
