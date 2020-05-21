#Code:

m= int(input())
s= str(input())
 
a=s.count("SF")
b=s.count("FS")
if a>b:
    print("YES")
else:
    print("NO")
