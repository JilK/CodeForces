#Code:

a, b= input().split()
li= list(map(int, input().split()))

li.sort(reverse=True)
test=[]
i=0
n=0
while i<len(li)-1:
    if li[i]-li[i+1]<=int(b):
        n=n+1
    else:
        break
    i=i+1
print(n+1)
