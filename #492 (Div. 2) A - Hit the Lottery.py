#Code:

p= int(input())
q=r=s=t=0
r=p//100
s=s+r
p=p-(r*100)
 
r=p//20
s=s+r
p=p-(r*20)
 
r=p//10
s=s+r
p=p-(r*10)
 
r=p//5
s=s+r
p=p-(r*5)
 
r=p//1
s=s+r
p=p-(r*1)
 
print(s)
