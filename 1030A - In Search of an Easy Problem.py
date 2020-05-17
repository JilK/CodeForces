#Code:

m=int(input())
a= [int(x) for x in input().split()]
b= ''.join(str(c) for c in a)
if str("1") in b:
    print("HARD")
else:
    print("EASY")
