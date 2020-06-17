#Code:

a= int(input())
b= int(input())

dist= abs(a-b)
tierd=0
c= dist//2


for i in range(c+1):
    tierd= tierd+ 2*i

if dist%2!=0:
    tierd = tierd + c+1
print(tierd)
