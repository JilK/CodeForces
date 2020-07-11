#Code;

l=[]
r=[]

for i in range(int(input())):
    lr= input().split()
    l.append(int(lr[0]))
    r.append(int(lr[1]))

x= min(l.count(0),l.count(1))
y=min(r.count(0),r.count(1))

print(x+y)
