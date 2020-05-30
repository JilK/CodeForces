# Code- 

p= int(input())
q= p//2
s=0
i=1
while i!=q+1:
    r = (p-i)//i
    if (r*i) +i==p:
        s=s+1
    
    i=i+1
 
print(s)
