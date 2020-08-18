#Code:

for i in range(int(input())):
    n,x,a,b= input().split()

    d= abs(int(a)- int(b))
    d= d+int(x)
    ans= min(int(n)-1 , d )
    print(ans)
