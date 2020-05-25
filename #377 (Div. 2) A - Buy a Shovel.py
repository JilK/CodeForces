#Code:

a= input().split()
n= int(a[0])
m= int(a[1])
i=1
d=1
while d!=0:
    b=n*i
    e=b%10
    c=(b-m)%10
    d=min(e,c)
    i=i+1
print(i-1)
