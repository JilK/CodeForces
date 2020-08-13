#Code :

n= int(input())
s= str(input())
count=0
x=1
for i in s:
    if int(i)%2==0:
        count= count+ s.index(i)+x
        x= x+ len(s[: s.index(i)])+1
        s= s[s.index(i)+1:]

        
print(count)
