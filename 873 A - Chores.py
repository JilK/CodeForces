#Code;

a,b,d = input().split()

c= list(map(int, input().split()))

c.sort()
r=0
while r<int(b):
    c.pop()
    r=r+1

print(sum(c)+ int(b)*int(d) )
