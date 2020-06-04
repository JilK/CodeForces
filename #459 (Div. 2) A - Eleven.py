#Code:

a= int(input())
fibo=[]
fibo.append(int(1))
fibo.append(int(1))

i=1

while fibo[i]<a:
    j= fibo[i-1] + fibo[i]
    fibo.append(j)
    i=i+1

ans=''

for i in range(1,a+1):
    if i in fibo:
        ans=ans+"O"
    else:
        ans= ans+'o'

print(ans)
