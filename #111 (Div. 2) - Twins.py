#Code:

n= int(input())
c= list(map(int,input().split()))
c.sort(reverse=True)
d=0
i=0
while d!=1:
    c1= c[:i+1]
    c2= c[i+1:]
    if sum(c1)>sum(c2):
        d==1
        break
    i=i+1
print(len(c1))
