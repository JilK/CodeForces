#Code - 

n= int(input())
c= str(input())
if c[0]==0:
    print(1)
elif '0' not in c:
    print(n)
else:
    x= c.split('0')[0]

    print(len(x)+1)
