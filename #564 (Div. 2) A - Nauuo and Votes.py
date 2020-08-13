#Code:

a,b,c = input().split()

if int(a)> int(b)+int(c):
    print("+")
elif int(b)>int(a)+int(c):
    print("-")
elif int(a)==int(b) and int(c)==0:
    print(0)
else:
    print("?")
