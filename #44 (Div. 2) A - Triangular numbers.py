#Code:

a = int(input())
test=[]
i=1
t_n=0
while t_n<=a:
    t_n= i*(i+1)//2
    test.append(t_n)
    i=i+1

if int(a) in test:
    print("YES")
else:
    print("NO")
