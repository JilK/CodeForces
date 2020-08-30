#Code:

n,a,b= input().split()

li= list(map(int, input().split()))
li.sort(reverse=True)

c= int(a)-1
x=int(li[int(a)])
xx=int(li[c]) 
if xx>x:
    print( xx-x )
else:
    print(0)
