#Code:

p= int(input())
 
if p==1:
    t= 'I hate it'
    print(t)
else:
    t='I hate'
    r=2
    while r<=p:
        if r%2==0:
            t= t + ' that I love'
        else:
            t=t + ' that I hate'
        r=r+1
    print(t+ ' it')
