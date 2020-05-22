#Code:

ab= input().split()
a= int(ab[0])
b= int(ab[1])
if a<b:
    c=b-a
    d= c//2
    print(a, d)
else:
    c=a-b
    d=c//2
    print(b, d)
